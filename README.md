# TestService-Render
Python server to grab and decode the output

Will name the files based on what the render camera is called 

# Requirements
If you want to use the Python file you need to have flask, json, and base64 packages installed

If you use the build in [releases] then you don't need anything other than Roblox Studio

# How to use
1. Run the Python file or a the [release] build
2. Put a RenderingTest inside of TestService
3. Use the properties Window to set the settings
4. Run the following command in the command bar to render
```lua
game.TestService:Run()
```

# Scripts
### Move the RenderingTest to your camera
```lua
local cam = workspace.CurrentCamera
local Rcam = game:GetService("TestService"):FindFirstChildOfClass("RenderingTest")

Rcam.CFrame = cam.CFrame
Rcam.FieldOfView = cam.FieldOfView
```

### Create a new RenderingTest on top of current camera
```lua
local cam = workspace.CurrentCamera
local Rcam = Instance.new("RenderingTest", game:GetService("TestService"))

Rcam.CFrame = cam.CFrame
Rcam.FieldOfView = cam.FieldOfView
```

# Info
The useless docs on the RenderingTest object: https://create.roblox.com/docs/reference/engine/classes/RenderingTest

Devforums asking for help: https://devforum.roblox.com/t/what-response-data-does-renderingtest-want/1555555

MaximumADHD's basic version writen in C#: https://gist.github.com/maximumadhd/1594e716dcafe06f37cf9e1d8fcb2c3c

# It running
[2023-03-31 14-36-39.webm](https://user-images.githubusercontent.com/67937010/229203772-48c09ccc-c7a2-46cb-9c92-249fe0218a05.webm)


[release]: "https://github.com/Roblox-Thot/TestService-Render/releases/latest"
[releases]: "https://github.com/Roblox-Thot/TestService-Render/releases"