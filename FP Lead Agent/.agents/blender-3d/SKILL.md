---
name: blender-3d
description: Helps plan, create, edit, and automate Blender 3D scenes, assets, materials, lighting, cameras, renders, geometry nodes, and Blender Python scripts. Use when the user asks for Blender work, 3D modeling guidance, scene setup, procedural assets, animation, rendering, camera composition, material design, or debugging Blender Python.
---

# Blender 3D

Use this skill for Blender-focused 3D work: modeling plans, scene direction, procedural creation, Blender Python scripts, materials, lighting, cameras, animation, and render setup.

## Workflow

1. Clarify the target output only when necessary: still render, animation, asset, product mockup, environment, game prop, or procedural setup.
2. Prefer Blender-native tools and Python APIs over vague manual instructions when the task can be automated.
3. Keep scripts self-contained and runnable in Blender's Python console or Text Editor.
4. Use real scene units, named objects, named collections, and non-destructive modifiers where practical.
5. Build from large forms to small details: composition, scale, silhouette, materials, lighting, camera, then polish.
6. For product or UI-related 3D, prioritize clean geometry, readable proportions, and controlled lighting over decorative complexity.
7. For procedural assets, expose important parameters at the top of the script.
8. When giving Blender Python, include setup cleanup only when the user wants a fresh generated scene.

## Blender Python Standards

- Import `bpy` and use `mathutils` where needed.
- Name objects, materials, cameras, lights, and collections clearly.
- Prefer functions for repeated object creation.
- Add bevels, weighted normals, and shade smooth when appropriate.
- Use Principled BSDF materials with explicit colors, roughness, metallic, alpha, and emission when useful.
- Set camera focal length, position, rotation, resolution, and render engine when producing a complete scene.
- Use area lights or HDRI-style world lighting for polished previews.
- Avoid destructive cleanup if the user is editing an existing `.blend` scene unless they ask for a new scene.

## Output Patterns

For code tasks, return:

1. A concise note about what the script creates or changes.
2. A complete Blender Python script.
3. Short run instructions: paste into Blender Text Editor and press Run Script, unless a different workflow is requested.

For art direction tasks, return:

1. Composition and silhouette guidance.
2. Modeling structure.
3. Materials and lighting.
4. Camera/render settings.
5. Polish checklist.

## Quality Checks

Before finalizing, check:

- Are object names understandable?
- Is the scale coherent?
- Is the camera aimed at the subject?
- Are materials distinct under the chosen lighting?
- Are modifiers applied only when necessary?
- Would the scene remain editable after the script runs?
