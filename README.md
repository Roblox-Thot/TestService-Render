# TestService-Render
Python server to grab and decode the TS output

# How to use
* Put a RenderingTest inside of TestService
* Use the properties Window to set the settings
* Run the following command in the command bar
```lua
game.TestService:Run()
```

# Scripts
### Move the RenderingTest to your camera
```lua
local cam = workspace:FindFirstChildOfClass("Camera")
local Rcam = game:GetService("TestService"):FindFirstChildOfClass("RenderingTest")

Rcam.CFrame = cam.CFrame
```

# Info
The useless docs on the RenderingTest object: https://create.roblox.com/docs/reference/engine/classes/RenderingTest

Devforums asking for help: https://devforum.roblox.com/t/what-response-data-does-renderingtest-want/1555555

# It running
[2023-03-31 14-36-39.webm](https://user-images.githubusercontent.com/67937010/229203772-48c09ccc-c7a2-46cb-9c92-249fe0218a05.webm)
