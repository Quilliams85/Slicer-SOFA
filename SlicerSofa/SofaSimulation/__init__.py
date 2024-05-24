import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.environ['SOFA_ROOT'] = script_dir + '/home/rafael/src/Slicer-SOFA/Release/inner-build/inner-build/lib/Slicer-5.7'

import Sofa
import SofaRuntime

from .SimulationController import SimulationController

__all__ = ["Sofa", "SofaRuntime", "SimulationController"]

# Make Sofa and SofaRuntime available in the global namespace
globals()['Sofa'] = Sofa
globals()['SofaRuntime'] = SofaRuntime