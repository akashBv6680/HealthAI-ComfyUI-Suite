import requests
import json
import uuid
from typing import Dict, Any, Optional
import time
import asyncio

class ComfyUIClient:
    def __init__(self, api_url: str = "http://localhost:8188"):
        self.api_url = api_url
        self.session = requests.Session()
        
    def queue_prompt(self, workflow: Dict[str, Any]) -> str:
        """Queue a prompt to ComfyUI and return prompt_id"""
        try:
            response = self.session.post(
                f"{self.api_url}/prompt",
                json={"prompt": workflow},
                timeout=10
            )
            response.raise_for_status()
            return response.json().get("prompt_id")
        except Exception as e:
            raise Exception(f"ComfyUI API Error: {str(e)}")
    
    def get_history(self, prompt_id: str) -> Optional[Dict]:
        """Get execution history for a prompt"""
        try:
            response = self.session.get(
                f"{self.api_url}/history/{prompt_id}",
                timeout=10
            )
            data = response.json()
            return data.get(prompt_id) if data else None
        except Exception as e:
            print(f"History fetch error: {e}")
            return None
    
    def wait_for_completion(self, prompt_id: str, timeout: int = 120) -> bool:
        """Poll and wait for prompt completion"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            history = self.get_history(prompt_id)
            if history and "outputs" in history:
                return True
            time.sleep(2)
        return False
    
    def get_images(self, prompt_id: str, node_id: str = "9") -> list:
        """Extract image filenames from completed prompt"""
        history = self.get_history(prompt_id)
        if not history or "outputs" not in history:
            return []
        
        outputs = history["outputs"]
        if str(node_id) not in outputs:
            return []
        
        images = []
        for img in outputs[str(node_id)].get("images", []):
            images.append(img["filename"])
        return images
    
    def get_image_url(self, filename: str) -> str:
        """Get full URL for an image"""
        return f"{self.api_url}/view?filename={filename}"

def get_risk_heatmap_workflow(patient_data: str) -> Dict[str, Any]:
    """Generate ComfyUI workflow for risk heatmap"""
    return {
        "1": {"class_type": "CheckpointLoaderSimple",
              "inputs": {"ckpt_name": "sdxl_turbo.safetensors"}},
        "2": {"class_type": "CLIPTextEncode",
              "inputs": {"text": f"medical risk heatmap, patient analysis: {patient_data}, anatomical diagram, clinical style",
                         "clip": ["1", 1]}},
        "3": {"class_type": "EmptyLatentImage",
              "inputs": {"width": 1024, "height": 1024, "batch_size": 1}},
        "4": {"class_type": "KSampler",
              "inputs": {"seed": 42, "steps": 20, "cfg": 7, "sampler_name": "euler",
                         "scheduler": "normal", "denoise": 1, "model": ["1", 0],
                         "positive": ["2", 0], "negative": ["5", 0],
                         "latent_image": ["3", 0]}},
        "5": {"class_type": "CLIPTextEncode",
              "inputs": {"text": "blurry, deformed, low quality",
                         "clip": ["1", 1]}},
        "6": {"class_type": "VAEDecode",
              "inputs": {"samples": ["4", 0], "vae": ["1", 2]}},
        "9": {"class_type": "SaveImage",
              "inputs": {"filename_prefix": "HealthAI_Risk",
                         "images": ["6", 0]}}
    }
