# GQ & Audemars Piguet: The Extraordinary Lab
Source: https://www.awwwards.com/gq-audemars-piguet-the-extraordinary-lab.html


## Jun 3, 2026

# GQ & AUDEMARS PIGUET: THE EXTRAORDINARY LAB


## Creating a Real-Time Cinematic Experience Around Audemars Piguet’s RD#5

Created in collaboration with Condé Nast for GQ and Audemars Piguet, “The Extraordinary Lab” was developed as an immersive interactive experience built around the RD#5.

From the beginning, the ambition behind the project was extremely clear. This could not feel like a traditional luxury campaign website or a classic product showcase. The experience needed to reflect the same level of precision, intensity, craftsmanship, and attention to detail associated with Audemars Piguet itself.

The goal was to create a cinematic WebGL experience combining storytelling, sound design, real-time rendering, interaction systems, and editorial content into a single immersive timeline.

For Immersive Garden, the challenge was particularly demanding. Audemars Piguet has an incredibly strong visual identity and extremely high expectations regarding rendering quality, materials, lighting, motion, and overall polish. Every reflection, texture, shadow, transition, and animation needed to feel precise while remaining fully interactive and performant across devices.

The project was developed over roughly three and a half months with a team of around ten people spanning creative direction, interaction design, WebGL development, technical direction, 3D production, rendering, shaders, motion systems, and sound integration.


## Building a Continuous Cinematic Timeline

Early concepts explored something closer to a lightweight editorial podcast interface where users could simply navigate through conversations and visuals. But as the project evolved, the timeline became the foundation of the entire experience.

Rather than separating the website into disconnected scenes or chapters, the entire experience was designed around a continuous cinematic track where users move forward and backward almost like navigating through a media player.

This approach became essential for reducing friction and preserving immersion.

As users scroll or drag through the experience, the timeline simultaneously controls:

Underneath this simplicity sat one of the biggest technical challenges of the project.

Because the experience was built around conversations between Jay Balvin and Cam Wolf, GQ Watch Editor, audio became a core layer of the navigation system itself.

The challenge was not simply playing sound while users moved through a website. The challenge was allowing users to freely navigate while preserving rhythm, pacing, and continuity across the experience.

If users quickly scrubbed through the project, the audio could not simply accelerate unnaturally alongside the animation. Instead, the system dynamically manages fades, pauses, synchronization states, and playback continuity depending on user behaviour.

A significant amount of invisible engineering work went into making the navigation feel intuitive, smooth, and effortless despite the complexity happening underneath.

What appears simple on the surface is actually a tightly choreographed system balancing interaction, rendering, storytelling, motion, and sound simultaneously.


## Designing Luxury Rendering in Real Time

Luxury watch projects introduce a very specific contradiction.

The product needs to remain physically accurate while somehow feeling even more cinematic and emotionally amplified than reality itself.

For “The Extraordinary Lab”, rendering the RD#5 became one of the most iterative parts of the production process.

The experience contains close-up product shots, dynamic lighting conditions, reflective materials, dark environments, camera transitions, and large-scale movements where the watch always needed to remain pristine.

At the same time, everything was rendered entirely in real time directly inside the browser.

This created a constant balancing act between:

The target throughout production was maintaining an extremely fluid 60 FPS experience, including on older mobile devices such as iPhone 11 and iPhone 12 generations.

Several rendering approaches and optimization techniques were explored throughout development, including:

Many solutions did not come from inventing entirely new technologies, but from intelligently combining existing rendering techniques while constantly negotiating against browser performance constraints.

One of the biggest challenges was preserving the luxurious visual fidelity expected by Audemars Piguet while still maintaining responsive interaction and fast loading times across devices.


## Theater.js and Collaborative Motion Systems

To orchestrate the experience, the team relied heavily on Theater.js as part of the production pipeline.

Rather than hardcoding every animation and transition directly into development workflows, Theater.js allowed designers and developers to collaboratively shape motion, pacing, interactions, transitions, camera movements, and timing directly inside the live experience.

This fundamentally changed the workflow.

Instead of separating creative decisions from implementation, design and development evolved simultaneously inside the same environment. Motion curves, timings, visual compositions, interface behaviour, and transitions could all be refined interactively against the final rendered experience itself.

For a project built around cinematic rhythm and synchronization, this level of control became extremely valuable.


## Sound as a Core Interaction Layer

Sound played a central role throughout the entire project.

Because the experience was structured around a podcast conversation, audio was never treated as a secondary layer added afterward. It became part of the interaction system itself.

The environments, pacing, transitions, and camera movements were all designed around rhythm and continuity.

For Immersive Garden, this became one of the most interesting aspects of the production process. The challenge was not simply creating an immersive 3D website, but building a synchronized audiovisual experience where interaction and sound continuously respond to one another.

The objective was ultimately emotional.

The experience needed to communicate the craftsmanship, precision, technical mastery, and obsessive attention to detail surrounding both the RD#5 and Audemars Piguet’s broader universe.


## Creating an Audemars Piguet Universe

Beyond the watch itself, the surrounding environments played a major role in shaping the atmosphere of the project.

Audemars Piguet wanted the experience to preserve the singular identity associated with the brand: dark, elegant, precise, immersive, and slightly electric at the same time.

The environments needed to feel futuristic without becoming stereotypical science fiction.

Large amounts of visual exploration, moodboarding, rendering studies, and iteration went into finding that balance.

The final spaces combine reflective materials, atmospheric lighting, industrial precision, oversized projections, cinematic transitions, and layered interface systems to create a universe that feels alive around the product rather than simply displaying it.

The ambition was never creating “3D for the sake of 3D”.

Every visual decision needed to remain coherent with the storytelling, the pacing, the product, and the emotional atmosphere surrounding the experience.


## AI-Assisted Production Experiments

Throughout the environments, users encounter projected silhouettes of Jay Balvin and Cam Wolf integrated directly into the scenes.

At the time of production, generative video tools were still rapidly evolving, and the project became an opportunity to experiment with AI-assisted production workflows.

The team explored techniques involving AI-generated projections, compositing experiments, green-screen prompting, and alpha-mask workflows to create abstract human silhouettes integrated into the environments.

At the same time, the project also reinforced an important limitation of AI within luxury production environments.

Precision matters.

Many early AI-generated outputs introduced inconsistencies that conflicted with the level of visual fidelity expected throughout the experience. In the end, most of the final project still relied heavily on traditional art direction, 3D production, rendering, compositing, interaction design, and human iteration.

Interestingly, “The Extraordinary Lab” also became one of the final large productions developed before AI tools became more deeply integrated into Immersive Garden’s broader internal workflows.


## Mobile Performance as a Core Constraint

Performance optimization was considered from the earliest stages of production.

Because the campaign would naturally circulate through editorial channels, social platforms, and mobile traffic, a large portion of users would first experience the project directly on smartphones.

This significantly influenced decisions across:

Creating a visually rich real-time WebGL experience that still feels fluid and responsive on mobile remains one of the most difficult challenges in interactive production.

Many of the most time-consuming details remain completely invisible to users:

Paradoxically, this invisible layer of polish often becomes what users emotionally perceive the most.


## Collaboration Between Creative and Technical Teams

“The Extraordinary Lab” was developed through close collaboration between Immersive Garden, Condé Nast, GQ, and Audemars Piguet.

Because the experience relied heavily on synchronization between storytelling, rendering, sound, interaction, motion systems, and editorial direction, creative and technical decisions constantly evolved together throughout production.

Condé Nast played an important role throughout the collaboration process, helping maintain consistency between editorial direction, campaign objectives, and the expectations surrounding the Audemars Piguet universe.

The collaboration itself became an important part of the project’s success.


## Pushing Interactive Storytelling Forward

Projects like “The Extraordinary Lab” reflect a broader evolution happening across luxury digital experiences.

Luxury storytelling online is no longer limited to static campaigns or traditional product pages. Users increasingly expect immersive experiences that feel reactive, cinematic, emotional, and alive in real time.

For Immersive Garden, the objective was never creating a technology showcase.

The objective was creating an experience where technology disappears behind rhythm, atmosphere, interaction, storytelling, and emotion.

Winning Site of the Month ultimately reflected the amount of depth, precision, iteration, and invisible craftsmanship layered throughout the project.

Not through excess.

But through coherence, rhythm, and attention to detail.


## Technologies Used

Front End
HTML, CSS, JavaScript

Rendering & Interaction
WebGL / Three.js / Theater.js / GSAP

3D Pipeline
Blender / Physically Based Rendering (PBR) workflows / HDR lighting

Rendering Techniques
Custom shaders / billboard reflections / parallax mapping / planar reflections

Motion Systems
Scroll-synchronised timelines / drag-based navigation systems

AI Assisted Production
AI-generated projection workflows and compositing experiments


## Company Info

Immersive Garden creates digital experiences that merge storytelling, interaction, and emerging technologies. Working across interactive design, real-time rendering, and immersive narratives, the studio develops projects that balance technical precision with emotional resonance, building experiences designed to be explored rather than simply viewed.

This website uses cookies to ensure you get the best experience on our website. Cookies Policy