from modules.command_router.router import route
from modules.assistant_orchestrator.orchestrator import ask
from modules.response_engine.response import success
from modules.event_bus.events import emit


def test_bearcore_flow():

    command = "etsi tietoa 3D tulostimista"


    routed = route(
        command
    )

    assert routed["success"] is True


    assistant = ask(
        command
    )

    assert assistant["success"] is True


    response = success(
        "Tutkimus käynnistetty"
    )

    assert response["success"] is True


    event = emit(
        "research_started",
        {
            "topic": "3D tulostimet"
        },
        "bearcore_flow"
    )


    assert event["name"] == "research_started"