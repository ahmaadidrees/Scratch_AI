import json
import zipfile
import io

def convert_to_scratch(ai_code):
    # Parse the AI code and create a script structure
    # For now, we'll use a simple example script
    script = {
        "AAAAA1": {
            "opcode": "event_whenflagclicked",
            "next": "AAAAA2",
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": True,
            "x": 0,
            "y": 0
        },
        "AAAAA2": {
            "opcode": "looks_say",
            "next": None,
            "parent": "AAAAA1",
            "inputs": {
                "MESSAGE": [1, [10, ai_code]]  # Use the AI code as the message
            },
            "fields": {},
            "shadow": False,
            "topLevel": False
        }
    }

    # Create the project JSON structure
    project = {
        "targets": [
            {
                "isStage": True,
                "name": "Stage",
                "variables": {},
                "lists": {},
                "broadcasts": {},
                "blocks": {},
                "comments": {},
                "currentCostume": 0,
                "costumes": [
                    {
                        "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
                        "name": "backdrop1",
                        "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
                        "dataFormat": "svg",
                        "rotationCenterX": 240,
                        "rotationCenterY": 180
                    }
                ],
                "sounds": [],
                "volume": 100,
                "layerOrder": 0,
                "tempo": 60,
                "videoTransparency": 50,
                "videoState": "on",
                "textToSpeechLanguage": None
            },
            {
                "isStage": False,
                "name": "Sprite1",
                "variables": {},
                "lists": {},
                "broadcasts": {},
                "blocks": script,
                "comments": {},
                "currentCostume": 0,
                "costumes": [
                    {
                        "assetId": "bcf454acf82e4504149f7ffe07081dbc",
                        "name": "costume1",
                        "bitmapResolution": 1,
                        "md5ext": "bcf454acf82e4504149f7ffe07081dbc.svg",
                        "dataFormat": "svg",
                        "rotationCenterX": 48,
                        "rotationCenterY": 50
                    }
                ],
                "sounds": [],
                "volume": 100,
                "layerOrder": 1,
                "visible": True,
                "x": 0,
                "y": 0,
                "size": 100,
                "direction": 90,
                "draggable": False,
                "rotationStyle": "all around"
            }
        ],
        "monitors": [],
        "extensions": [],
        "meta": {
            "semver": "3.0.0",
            "vm": "0.2.0",
            "agent": "Scratch AI Converter"
        }
    }

    # Create a in-memory zip file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        # Add project.json to the zip file
        zip_file.writestr("project.json", json.dumps(project))

    # Get the zip file content
    zip_buffer.seek(0)
    return zip_buffer.getvalue()