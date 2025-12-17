
from plantuml import PlantUML

def render_plantuml(plantuml_code: str, output_path: str = "uml.png"):
    """
    Render PlantUML code to an image using the public PlantUML server.
    """
    server = PlantUML(url="https://www.plantuml.com/plantuml/svg/")

    image_data = server.processes(plantuml_code)
    print(image_data)
    
    with open(output_path, "wb") as f:
        f.write(image_data)

if __name__ == "__main__":
    plantuml_code = """
    @startuml
    class User {
      +name: String
      +email: String
      +login()
    }
    @enduml
    """
    render_plantuml(plantuml_code, "example_uml.svg")