from langchain_core.prompts import PromptTemplate

def get_template(image_prompt:str) -> PromptTemplate:
    eval_prompt = """Evaluate this image based on the following criteria:

                    **Your task:** Determine if this image looks natural and realistic, or if it appears AI-generated.

                    {image_prompt}

                    **Look for these signs of AI generation (RED FLAGS):**
                    - Unnatural skin texture (too smooth, plastic-like, or waxy appearance)
                    - Strange hands or fingers (wrong number, odd positioning, merged digits)
                    - Inconsistent lighting or shadows that don't match the scene
                    - Blurry or distorted details, especially in the background
                    - Odd facial features (asymmetrical eyes, unnatural teeth, strange ears)
                    - Text or writing that is gibberish or malformed
                    - Repeating patterns that don't make logical sense
                    - Objects that blend unnaturally into each other
                    - Impossible reflections or perspectives
                    - Overly perfect symmetry or composition that feels artificial

                    **Signs of natural/authentic images (GOOD SIGNS):**
                    - Realistic skin pores, texture, and imperfections
                    - Natural lighting with consistent shadows
                    - Coherent background details that make sense
                    - Proper hand and finger anatomy
                    - Authentic facial expressions and proportions
                    - Real-world "messiness" (dust, wear, natural disorder)
                    - Consistent depth of field and focus

                    **Provide your evaluation in this format:**
                    1. **Overall Assessment:** Does this look AI-generated or natural? (Natural/AI-Generated/Uncertain)
                    2. **Confidence Level:** How confident are you? (High/Medium/Low)
                    3. **Key Observations:** List 3-5 specific details that support your assessment
                    4. **Final Verdict:** PASS or FAIL (PASS = looks natural, FAIL = looks AI-generated)

                    Be strict in your evaluation. When in doubt, lean towards FAIL."""
    template = PromptTemplate.from_template(eval_prompt).format(image_prompt=image_prompt)

    return template