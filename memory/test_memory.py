from memory.memory_store import MemoryStore

def test_memory_store():
    mem = MemoryStore()

    input_id = "test_input_123"
    
    # Save input metadata
    metadata = {
        "source": "email",
        "timestamp": "2025-05-31T12:00:00Z",
        "classification": "complaint"
    }
    mem.save_input_metadata(input_id, metadata)

    # Save extracted fields
    fields = {
        "sender": "user@example.com",
        "tone": "angry",
        "urgency": "high"
    }
    mem.save_extracted_fields(input_id, fields)

    # Save decision trace
    trace = {
        "step": "email_agent",
        "decision": "trigger_escalation"
    }
    mem.save_decision_trace(input_id, trace)

    # Save follow-up action
    action = {
        "action": "POST /crm/escalate",
        "status": "success"
    }
    mem.save_follow_up_action(input_id, action)

    # Load and print everything
    all_data = mem.load_all(input_id)
    print("=== Memory Store Contents ===")
    print(all_data)

if __name__ == "__main__":
    test_memory_store()
