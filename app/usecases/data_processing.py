from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData


def process_agent_data(agent_data: AgentData) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    try:
        y_val = agent_data.accelerometer.y
        if y_val <= 10352.108:
            road_state = "В межах норми"
        else:
            road_state = "Велика яма"
        return ProcessedAgentData(road_state=road_state, agent_data=agent_data)
    except Exception as e:
        print(f"An error occurred while processing agent data: {e}")
