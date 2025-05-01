from classes import *

tool_box = ToolBox()

hammer = Hammer(color="gray")
screw_driver = Screwdriver()

tool_box.add_tool(screw_driver)
tool_box.add_tool(hammer)

screw = Screw()
print(str(screw))
screw_driver.tighten(screw)
print(str(screw))


nail = Nail()
print(str(nail))
hammer.hammer_in(nail)
print(str(nail))

