from langchain_core.prompts import PromptTemplate

def get_template(image_prompt:str) -> PromptTemplate:
    eval_prompt = """You are a Quality Assurance Specialist for AI Imagery.
    
                    **Goal:** Evaluate if the generated image strictly matches the intended prompt and meets professional quality standards.

                    **Intended Prompt (Ground Truth):**
                    {image_prompt}

                    **Evaluation Steps:**
                    1. **Prompt Fidelity:** Does the image actually show what was asked? (e.g., if prompt says "red hat", is there a red hat?)
                    2. **Realism/Style Adherence:** Does the style match the requested art direction (e.g., Cinematic, 3D Render)?
                    3. **Anatomy & Physics:** Check for hands, limbs, gravity, and reflections.
                    4. **Artifacts:** Check for "glitching", random floating objects, or garbled text.
                    
                    **Critical Fail Conditions (Automatic FAIL):**
                    - [ ] Extra or missing limbs on humans/animals.
                    - [ ] Severe facial distortion (unless specified as horror).
                    - [ ] Visible text/watermarks when none were requested.
                    - [ ] Blurry main subject.

                    **Provide your evaluation in this format:**
                    1. **Score (1-10):** <score>
                    2. **Missing Elements:** <list any prompt details missing from image>
                    3. **Unwanted Elements:** <list any artifacts or hallucinations>
                    4. **Final Verdict:** "PASS" (if Score >= 8) or "FAIL" (if Score < 8)."""
    template = PromptTemplate.from_template(eval_prompt).format(image_prompt=image_prompt)

    return template