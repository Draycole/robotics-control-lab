import mujoco
import mujoco.viewer
import time

xml = """
<mujoco>
    <option gravity="0 0 -9.81"/>

    <asset>
        <!-- sky -->
        <texture type="skybox" builtin="gradient" rgb1="0.3 0.5 0.7" rgb2="0 0 0" width="512" height="3072"/>
        
        <!-- floor texture; grey checkerboard pattern -->
        <texture name="texplane" type="2d" builtin="checker" rgb1="0.2 0.3 0.4" rgb2="0.1 0.2 0.3" width="300" height="300" mark="edge" markrgb="0.8 0.8 0.8"/>
        
        <!-- floor material; repeats the checkerboard texture -->
        <material name="matplane" texture="texplane" texuniform="true" texrepeat="5 5" reflectance="0.2"/>
    </asset>

    <worldbody>
        <geom name="floor" type="plane" size="0 0 .25" material="matplane"/>

        <body name="link1" pos="0 0 2.5">
            <joint name="hinge1" type="hinge" axis="0 1 0"/>
            <geom type="capsule" fromto="0 0 0 0 0 -1" size="0.02" mass="1"/>
            
            <body name="link2" pos="0 0 -1">
                <joint name="hinge2" type="hinge" axis="0 1 0"/>
                <geom type="capsule" fromto="0 0 0 0 0 -1" size="0.02" mass="1"/>
            </body> 
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

data.qpos[0] = 2
data.qpos[1] = 0

with mujoco.viewer.launch_passive(model, data) as viewer:

    while viewer.is_running():

        mujoco.mj_step(model, data)

        viewer.sync()

        time.sleep(model.opt.timestep)