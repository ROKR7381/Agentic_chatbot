import sys
from pathlib import Path
     
# Get the absolute path to the src directory
src_path = Path(__file__).parent.resolve() / "src"
      # Add the src directory to the Python path
sys.path.insert(0, str(src_path))
     

from src.langgraphagenticai.main import load_langgraph_agenticai_app
import src

if __name__=="__main__":
    load_langgraph_agenticai_app()