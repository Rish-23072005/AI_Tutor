from typing import List, Dict, Any

class ValidationError(Exception):
    def __init__(self, message, error_code="validation_error", details=None):
        super().__init__(message)
        self.error_code = error_code
        self.details = details

class UserInfoValidator:
    @staticmethod
    def validate(user_info: Dict[str, Any]):
        required = ["user_id", "name", "grade_level", "learning_style_summary", "emotional_state_summary", "mastery_level_summary"]
        for key in required:
            if key not in user_info or not isinstance(user_info[key], str) or not user_info[key].strip():
                raise ValidationError(f"Missing or invalid user_info field: {key}")
        if len(user_info["learning_style_summary"]) > 1000 or len(user_info["emotional_state_summary"]) > 1000 or len(user_info["mastery_level_summary"]) > 1000:
            raise ValidationError("Summary fields too long")

class ChatHistoryValidator:
    @staticmethod
    def validate(chat_history: List[Dict[str, Any]]):
        if not isinstance(chat_history, list) or not (1 <= len(chat_history) <= 10):
            raise ValidationError("Chat history must be 1-10 messages")
        for msg in chat_history:
            if msg.get("role") not in ["user", "assistant"] or not isinstance(msg.get("content"), str) or not msg["content"].strip():
                raise ValidationError("Invalid chat history message")

class EducationalContextValidator:
    TEACHING_STYLES = ["Direct", "Socratic", "Visual", "Flipped Classroom"]
    EMOTIONAL_STATES = ["Focused", "Anxious", "Confused", "Tired"]
    @staticmethod
    def validate(teaching_style: str, emotional_state: str, mastery_level: int):
        if teaching_style not in EducationalContextValidator.TEACHING_STYLES:
            raise ValidationError("Invalid teaching style")
        if emotional_state not in EducationalContextValidator.EMOTIONAL_STATES:
            raise ValidationError("Invalid emotional state")
        if not (1 <= mastery_level <= 10):
            raise ValidationError("Mastery level must be 1-10")

class NoteMakerValidator:
    NOTE_STYLES = ["outline", "bullet_points", "narrative", "structured"]
    @staticmethod
    def validate(params: Dict[str, Any]):
        UserInfoValidator.validate(params["user_info"])
        ChatHistoryValidator.validate(params["chat_history"])
        if params["note_taking_style"] not in NoteMakerValidator.NOTE_STYLES:
            raise ValidationError("Invalid note_taking_style")
        if not isinstance(params.get("topic"), str) or not params["topic"].strip():
            raise ValidationError("Missing or invalid topic")
        if not isinstance(params.get("subject"), str) or not params["subject"].strip():
            raise ValidationError("Missing or invalid subject")
        # Optional booleans
        if "include_examples" in params and not isinstance(params["include_examples"], bool):
            raise ValidationError("include_examples must be boolean")
        if "include_analogies" in params and not isinstance(params["include_analogies"], bool):
            raise ValidationError("include_analogies must be boolean")

class FlashcardGeneratorValidator:
    DIFFICULTY = ["easy", "medium", "hard"]
    @staticmethod
    def validate(params: Dict[str, Any]):
        UserInfoValidator.validate(params["user_info"])
        if not isinstance(params.get("topic"), str) or not params["topic"].strip():
            raise ValidationError("Missing or invalid topic")
        if not isinstance(params.get("count"), int) or not (1 <= params["count"] <= 20):
            raise ValidationError("Count must be 1-20")
        if params["difficulty"] not in FlashcardGeneratorValidator.DIFFICULTY:
            raise ValidationError("Invalid difficulty")
        if not isinstance(params.get("subject"), str) or not params["subject"].strip():
            raise ValidationError("Missing or invalid subject")
        if "include_examples" in params and not isinstance(params["include_examples"], bool):
            raise ValidationError("include_examples must be boolean")

class ConceptExplainerValidator:
    DEPTH = ["basic", "intermediate", "advanced", "comprehensive"]
    @staticmethod
    def validate(params: Dict[str, Any]):
        UserInfoValidator.validate(params["user_info"])
        ChatHistoryValidator.validate(params["chat_history"])
        if not isinstance(params.get("concept_to_explain"), str) or not params["concept_to_explain"].strip():
            raise ValidationError("Missing or invalid concept_to_explain")
        if not isinstance(params.get("current_topic"), str) or not params["current_topic"].strip():
            raise ValidationError("Missing or invalid current_topic")
        if params["desired_depth"] not in ConceptExplainerValidator.DEPTH:
            raise ValidationError("Invalid desired_depth")

def validate_tool_params(tool: str, params: Dict[str, Any]):
    if tool == "note_maker":
        NoteMakerValidator.validate(params)
    elif tool == "flashcard_generator":
        FlashcardGeneratorValidator.validate(params)
    elif tool == "concept_explainer":
        ConceptExplainerValidator.validate(params)
    else:
        raise ValidationError("Unknown tool type")
def validate_prompt(prompt: str):
    if not prompt or not prompt.strip():
        raise ValueError('Prompt must not be empty')
    if len(prompt) > 5000:
        raise ValueError('Prompt too long (limit 5000 chars)')
