const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const BASE_DIR = 'C:\\Users\\HP\\Downloads\\Components';
const REGISTRY_PATH = path.join(BASE_DIR, 'components_ai_registry.json');
const THUMBNAILS_DIR = path.join(BASE_DIR, 'public', 'thumbnails');

if (!fs.existsSync(THUMBNAILS_DIR)) {
    fs.mkdirSync(THUMBNAILS_DIR, { recursive: true });
}

async function verifyAndCapture() {
    if (!fs.existsSync(REGISTRY_PATH)) {
        console.error('[ERROR] components_ai_registry.json not found! Run scripts/build_component_studio.py first.');
        process.exit(1);
    }

    const registry = JSON.parse(fs.readFileSync(REGISTRY_PATH, 'utf8'));
    console.log(`[PLAYWRIGHT CAPTURE] Loaded ${registry.length} components. Launching headless browser...`);

    const browser = await chromium.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const context = await browser.newContext({
        viewport: { width: 1280, height: 720 },
        deviceScaleFactor: 1
    });

    const page = await context.newPage();
    let successCount = 0;
    let errorCount = 0;

    for (let i = 0; i < registry.length; i++) {
        const item = registry[i];
        const compId = item.id;
        const entryUrl = item.entry_url;
        const thumbnailPath = path.join(THUMBNAILS_DIR, `${compId}.png`);

        if (!entryUrl) {
            console.log(`[SKIP ${compId}] No static entry URL (NPM Build Required).`);
            continue;
        }

        const fullUrl = `http://127.0.0.1:8080/${entryUrl}`;
        const pageErrors = [];
        const consoleErrors = [];

        page.removeAllListeners('pageerror');
        page.removeAllListeners('console');

        page.on('pageerror', err => pageErrors.push(err.message));
        page.on('console', msg => {
            if (msg.type() === 'error') {
                consoleErrors.push(msg.text());
            }
        });

        try {
            console.log(`[${i+1}/${registry.length}] Navigating to ${compId}: ${item.name} ...`);
            await page.goto(fullUrl, { waitUntil: 'domcontentloaded', timeout: 10000 });

            // User Instruction Q3: Wait exactly 3.0 seconds for WebGL, Canvas & GSAP shaders to initialize
            await page.waitForTimeout(3000);

            // Screenshot capture
            await page.screenshot({ path: thumbnailPath, fullPage: false });

            if (pageErrors.length > 0) {
                console.log(`  └─ [WARNING ${compId}] ${pageErrors.length} JS errors: ${pageErrors[0].slice(0, 100)}`);
                item.health_note = `JS Error: ${pageErrors[0].slice(0, 100)}`;
                errorCount++;
            } else {
                item.health_note = 'Clean Load (3.0s visual capture)';
                successCount++;
            }
        } catch (err) {
            console.error(`  └─ [FAILED ${compId}] Could not load ${fullUrl}: ${err.message.slice(0, 100)}`);
            item.health_note = `Load Error: ${err.message.slice(0, 100)}`;
            errorCount++;
        }
    }

    // Save updated health notes to registry
    fs.writeFileSync(REGISTRY_PATH, JSON.stringify(registry, null, 2), 'utf8');

    await browser.close();
    console.log(`\n==================================================`);
    console.log(`[PLAYWRIGHT COMPLETE] Clean Screenshots: ${successCount} | Warnings/Errors: ${errorCount}`);
    console.log(`Thumbnails saved to: ${THUMBNAILS_DIR}`);
    console.log(`==================================================\n`);
}

verifyAndCapture().catch(err => {
    console.error('[FATAL PLAYWRIGHT ERROR]', err);
    process.exit(1);
});
