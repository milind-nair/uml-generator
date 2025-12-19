from plantuml import PlantUML
import os

def render_plantuml(plantuml_code: str, output_path: str = "uml.png"):
    """
    Render PlantUML code to an image using the public PlantUML server.
    """
    server = PlantUML(url="https://www.plantuml.com/plantuml/png/")

    try:
        image_data = server.processes(plantuml_code)
        
        # The library returns bytes on success and a string with an error on failure.
        if isinstance(image_data, bytes):
            with open(output_path, "wb") as f:
                f.write(image_data)
            print(f"UML diagram saved to {os.path.abspath(output_path)}")
        else:
            print(f"Error rendering PlantUML: {image_data}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

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
    render_plantuml(plantuml_code, "example_uml.png")
