# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import os
import numpy as np
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

print('*** Start to run job...')

currentdir=os.getcwd()
efilename=''
for subdir,dirs,files in os.walk(currentdir):
	for file in files:
		if '.e' in file:
			efilename=file
			break

###########################################
### Settings for plot
###########################################
CameraX,CameraY = 9.674798308212488, 8.306987331087002
CameraScale = 8.42359953337398

TitleFontSize = 8 # integer
LabelFontSize = 5 # integer
ScalarBarThickness = 8 # integer
ScalarBarLength = 0.25 # float

prefix='50-'



print('***    we are in:',currentdir)
print('***    efilename=',efilename)

# create a new 'ExodusIIReader'
filename=currentdir+'/'+efilename
circle100_outee = ExodusIIReader(FileName=[filename])
circle100_outee.ElementVariables = []
circle100_outee.PointVariables = []
circle100_outee.GlobalVariables = []
circle100_outee.NodeSetArrayStatus = []
circle100_outee.SideSetArrayStatus = []

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on circle100_outee
circle100_outee.ElementVariables = ['Damage', 'DamageN', 'DamageT', 'HyStress', 'MaxJumpLocal_', 'MaxPrinStress', 'MinPrinStress', 'TractionLocal_', 'flux', 'fluxvec_', 'normvec_', 'vonMises']
circle100_outee.PointVariables = ['Damage', 'DamageN', 'DamageT', 'HyStress', 'J_', 'MaxJumpLocal_', 'MaxPrinStress', 'MinPrinStress', 'TractionLocal_', 'c', 'disp_', 'flux', 'fluxvec_', 'mu', 'normvec_', 'vonMises']
circle100_outee.GlobalVariables = ['Damage', 'Damage0', 'DamageN', 'DamageT', 'cs', 'soc']
circle100_outee.ElementBlocks = ['Unnamed block ID: 1 Type: TRI3', 'Unnamed block ID: 2 Type: TRI3', 'Unnamed block ID: 3 Type: TRI3', 'Unnamed block ID: 4 Type: TRI3', 'Unnamed block ID: 5 Type: TRI3', 'Unnamed block ID: 6 Type: TRI3', 'Unnamed block ID: 7 Type: TRI3', 'Unnamed block ID: 8 Type: TRI3', 'Unnamed block ID: 9 Type: TRI3', 'Unnamed block ID: 10 Type: TRI3', 'Unnamed block ID: 11 Type: TRI3', 'Unnamed block ID: 12 Type: TRI3', 'Unnamed block ID: 13 Type: TRI3', 'Unnamed block ID: 14 Type: TRI3', 'Unnamed block ID: 15 Type: TRI3', 'Unnamed block ID: 16 Type: TRI3', 'Unnamed block ID: 17 Type: TRI3', 'Unnamed block ID: 18 Type: TRI3', 'Unnamed block ID: 19 Type: TRI3', 'Unnamed block ID: 20 Type: TRI3', 'Unnamed block ID: 21 Type: TRI3', 'Unnamed block ID: 22 Type: TRI3', 'Unnamed block ID: 23 Type: TRI3', 'Unnamed block ID: 24 Type: TRI3', 'Unnamed block ID: 25 Type: TRI3', 'Unnamed block ID: 26 Type: TRI3', 'Unnamed block ID: 27 Type: TRI3', 'Unnamed block ID: 28 Type: TRI3', 'Unnamed block ID: 29 Type: TRI3', 'Unnamed block ID: 30 Type: TRI3', 'Unnamed block ID: 31 Type: TRI3', 'Unnamed block ID: 32 Type: TRI3', 'Unnamed block ID: 33 Type: TRI3', 'Unnamed block ID: 34 Type: TRI3', 'Unnamed block ID: 35 Type: TRI3', 'Unnamed block ID: 36 Type: TRI3', 'Unnamed block ID: 37 Type: TRI3', 'Unnamed block ID: 38 Type: TRI3', 'Unnamed block ID: 39 Type: TRI3', 'Unnamed block ID: 40 Type: TRI3', 'Unnamed block ID: 41 Type: TRI3', 'Unnamed block ID: 42 Type: TRI3', 'Unnamed block ID: 43 Type: TRI3', 'Unnamed block ID: 44 Type: TRI3', 'Unnamed block ID: 45 Type: TRI3', 'Unnamed block ID: 46 Type: TRI3', 'Unnamed block ID: 47 Type: TRI3', 'Unnamed block ID: 48 Type: TRI3', 'Unnamed block ID: 49 Type: TRI3', 'Unnamed block ID: 50 Type: TRI3', 'Unnamed block ID: 51 Type: TRI3', 'Unnamed block ID: 52 Type: TRI3', 'Unnamed block ID: 53 Type: TRI3', 'Unnamed block ID: 54 Type: TRI3', 'Unnamed block ID: 55 Type: TRI3', 'Unnamed block ID: 56 Type: TRI3', 'Unnamed block ID: 57 Type: TRI3', 'Unnamed block ID: 58 Type: TRI3', 'Unnamed block ID: 59 Type: TRI3', 'Unnamed block ID: 60 Type: TRI3', 'Unnamed block ID: 61 Type: TRI3', 'Unnamed block ID: 62 Type: TRI3', 'Unnamed block ID: 63 Type: TRI3', 'Unnamed block ID: 64 Type: TRI3', 'Unnamed block ID: 65 Type: TRI3', 'Unnamed block ID: 66 Type: TRI3', 'Unnamed block ID: 67 Type: TRI3', 'Unnamed block ID: 68 Type: TRI3', 'Unnamed block ID: 69 Type: TRI3', 'Unnamed block ID: 70 Type: TRI3', 'Unnamed block ID: 71 Type: TRI3', 'Unnamed block ID: 72 Type: TRI3', 'Unnamed block ID: 73 Type: TRI3', 'Unnamed block ID: 74 Type: TRI3', 'Unnamed block ID: 75 Type: TRI3', 'Unnamed block ID: 76 Type: TRI3', 'Unnamed block ID: 77 Type: TRI3', 'Unnamed block ID: 78 Type: TRI3', 'Unnamed block ID: 79 Type: TRI3', 'Unnamed block ID: 80 Type: TRI3', 'Unnamed block ID: 81 Type: TRI3', 'Unnamed block ID: 82 Type: TRI3', 'Unnamed block ID: 83 Type: TRI3', 'Unnamed block ID: 84 Type: TRI3', 'Unnamed block ID: 85 Type: TRI3', 'Unnamed block ID: 86 Type: TRI3', 'Unnamed block ID: 87 Type: TRI3', 'Unnamed block ID: 88 Type: TRI3', 'Unnamed block ID: 89 Type: TRI3', 'Unnamed block ID: 90 Type: TRI3', 'Unnamed block ID: 91 Type: TRI3', 'Unnamed block ID: 92 Type: TRI3', 'Unnamed block ID: 93 Type: TRI3', 'Unnamed block ID: 94 Type: TRI3', 'Unnamed block ID: 95 Type: TRI3', 'Unnamed block ID: 96 Type: TRI3', 'Unnamed block ID: 97 Type: TRI3', 'Unnamed block ID: 98 Type: TRI3', 'Unnamed block ID: 99 Type: TRI3', 'Unnamed block ID: 100 Type: TRI3']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1105, 954]

# show data in view
circle100_outeeDisplay = Show(circle100_outee, renderView1)

# trace defaults for the display properties.
circle100_outeeDisplay.Representation = 'Surface'
circle100_outeeDisplay.ColorArrayName = [None, '']
circle100_outeeDisplay.OSPRayScaleArray = 'Damage'
circle100_outeeDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
circle100_outeeDisplay.SelectOrientationVectors = 'Damage'
circle100_outeeDisplay.ScaleFactor = 1.6401897430419923
circle100_outeeDisplay.SelectScaleArray = 'Damage'
circle100_outeeDisplay.GlyphType = 'Arrow'
circle100_outeeDisplay.GlyphTableIndexArray = 'Damage'
circle100_outeeDisplay.GaussianRadius = 0.08200948715209962
circle100_outeeDisplay.SetScaleArray = ['POINTS', 'Damage']
circle100_outeeDisplay.ScaleTransferFunction = 'PiecewiseFunction'
circle100_outeeDisplay.OpacityArray = ['POINTS', 'Damage']
circle100_outeeDisplay.OpacityTransferFunction = 'PiecewiseFunction'
circle100_outeeDisplay.DataAxesGrid = 'GridAxesRepresentation'
circle100_outeeDisplay.SelectionCellLabelFontFile = ''
circle100_outeeDisplay.SelectionPointLabelFontFile = ''
circle100_outeeDisplay.PolarAxes = 'PolarAxesRepresentation'
circle100_outeeDisplay.ScalarOpacityUnitDistance = 0.8995245905011773

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
circle100_outeeDisplay.DataAxesGrid.XTitleFontFile = ''
circle100_outeeDisplay.DataAxesGrid.YTitleFontFile = ''
circle100_outeeDisplay.DataAxesGrid.ZTitleFontFile = ''
circle100_outeeDisplay.DataAxesGrid.XLabelFontFile = ''
circle100_outeeDisplay.DataAxesGrid.YLabelFontFile = ''
circle100_outeeDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
circle100_outeeDisplay.PolarAxes.PolarAxisTitleFontFile = ''
circle100_outeeDisplay.PolarAxes.PolarAxisLabelFontFile = ''
circle100_outeeDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
circle100_outeeDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [CameraX,CameraY, 10000.0]
renderView1.CameraFocalPoint = [CameraX,CameraY, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(circle100_outeeDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
circle100_outeeDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.AnnotationsInitialized = 1
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# Properties modified on vtkBlockColorsLUT
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5000076295109483, 0.7499961852445258, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483]
vtkBlockColorsLUT.IndexedOpacities = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

animationScene1.GoToLast()

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]

# create a new 'Calculator'
calculator1 = Calculator(Input=circle100_outee)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'd'
calculator1.Function = 'Damage*1.1'

# show data in view
calculator1Display = Show(calculator1, renderView1)

# get color transfer function/color map for 'd'
dLUT = GetColorTransferFunction('d')
dLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5377734148464623, 0.865003, 0.865003, 0.865003, 1.0755468296929247, 0.705882, 0.0156863, 0.14902]
dLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'd'
dPWF = GetOpacityTransferFunction('d')
dPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0755468296929247, 1.0, 0.5, 0.0]
dPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'd']
calculator1Display.LookupTable = dLUT
calculator1Display.OSPRayScaleArray = 'd'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'Damage'
calculator1Display.ScaleFactor = 1.666371251642704
calculator1Display.SelectScaleArray = 'd'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'd'
calculator1Display.GaussianRadius = 0.0833185625821352
calculator1Display.SetScaleArray = ['POINTS', 'd']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'd']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.SelectionCellLabelFontFile = ''
calculator1Display.SelectionPointLabelFontFile = ''
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = dPWF
calculator1Display.ScalarOpacityUnitDistance = 0.9119555180424688

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.XTitleFontFile = ''
calculator1Display.DataAxesGrid.YTitleFontFile = ''
calculator1Display.DataAxesGrid.ZTitleFontFile = ''
calculator1Display.DataAxesGrid.XLabelFontFile = ''
calculator1Display.DataAxesGrid.YLabelFontFile = ''
calculator1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator1Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator1Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator1Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(circle100_outee, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator2 = Calculator(Input=calculator1)
calculator2.Function = ''

# Properties modified on calculator2
calculator2.ResultArrayName = 'RealStress'
calculator2.Function = 'MaxPrinStress*87.17'

# show data in view
calculator2Display = Show(calculator2, renderView1)

# get color transfer function/color map for 'RealStress'
realStressLUT = GetColorTransferFunction('RealStress')
realStressLUT.RGBPoints = [-121.05289334717823, 0.231373, 0.298039, 0.752941, 139.80187843364922, 0.865003, 0.865003, 0.865003, 400.65665021447666, 0.705882, 0.0156863, 0.14902]
realStressLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RealStress'
realStressPWF = GetOpacityTransferFunction('RealStress')
realStressPWF.Points = [-121.05289334717823, 0.0, 0.5, 0.0, 400.65665021447666, 1.0, 0.5, 0.0]
realStressPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['POINTS', 'RealStress']
calculator2Display.LookupTable = realStressLUT
calculator2Display.OSPRayScaleArray = 'RealStress'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'Damage'
calculator2Display.ScaleFactor = 1.666371251642704
calculator2Display.SelectScaleArray = 'RealStress'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'RealStress'
calculator2Display.GaussianRadius = 0.0833185625821352
calculator2Display.SetScaleArray = ['POINTS', 'RealStress']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'RealStress']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.SelectionCellLabelFontFile = ''
calculator2Display.SelectionPointLabelFontFile = ''
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityFunction = realStressPWF
calculator2Display.ScalarOpacityUnitDistance = 0.9119555180424688

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator2Display.DataAxesGrid.XTitleFontFile = ''
calculator2Display.DataAxesGrid.YTitleFontFile = ''
calculator2Display.DataAxesGrid.ZTitleFontFile = ''
calculator2Display.DataAxesGrid.XLabelFontFile = ''
calculator2Display.DataAxesGrid.YLabelFontFile = ''
calculator2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator2Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator2Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator2Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'c'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(realStressLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
calculator2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'c'
cLUT = GetColorTransferFunction('c')
cLUT.RGBPoints = [0.3949416867360376, 0.231373, 0.298039, 0.752941, 0.6976877748590242, 0.865003, 0.865003, 0.865003, 1.0004338629820109, 0.705882, 0.0156863, 0.14902]
cLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'c'
cPWF = GetOpacityTransferFunction('c')
cPWF.Points = [0.3949416867360376, 0.0, 0.5, 0.0, 1.0004338629820109, 1.0, 0.5, 0.0]
cPWF.ScalarRangeInitialized = 1

# get color legend/bar for cLUT in view renderView1
cLUTColorBar = GetScalarBar(cLUT, renderView1)
cLUTColorBar.Title = 'c'
cLUTColorBar.ComponentTitle = ''
cLUTColorBar.TitleFontFile = ''
cLUTColorBar.LabelFontFile = ''

# Properties modified on cLUTColorBar
cLUTColorBar.WindowLocation = 'LowerLeftCorner'
cLUTColorBar.Title = '$C/C_{max}$'
cLUTColorBar.HorizontalTitle = 1

# Properties modified on cLUTColorBar
cLUTColorBar.WindowLocation = 'LowerRightCorner'

# Properties modified on cLUTColorBar
cLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
cLUTColorBar.TitleFontFamily = 'Times'
cLUTColorBar.TitleFontSize = TitleFontSize
cLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
cLUTColorBar.LabelFontFamily = 'Times'
cLUTColorBar.LabelFontSize = LabelFontSize

# Properties modified on cLUTColorBar
cLUTColorBar.RangeLabelFormat = '%-#6.1f'

# Properties modified on cLUTColorBar
cLUTColorBar.ScalarBarThickness = ScalarBarThickness
cLUTColorBar.ScalarBarLength = ScalarBarLength

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
cLUT.ApplyPreset('jet', True)

# Properties modified on cLUTColorBar
cLUTColorBar.DrawTickLabels = 0

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'd'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(cLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
calculator2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
dLUT.ApplyPreset('Rainbow Uniform', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
dLUT.ApplyPreset('Rainbow Uniform', True)

# get color legend/bar for dLUT in view renderView1
dLUTColorBar = GetScalarBar(dLUT, renderView1)
dLUTColorBar.Title = 'd'
dLUTColorBar.ComponentTitle = ''
dLUTColorBar.TitleFontFile = ''
dLUTColorBar.LabelFontFile = ''

# Properties modified on dLUTColorBar
dLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
dLUTColorBar.TitleFontFamily = 'Times'
dLUTColorBar.TitleFontSize = TitleFontSize
dLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
dLUTColorBar.LabelFontFamily = 'Times'
dLUTColorBar.LabelFontSize = LabelFontSize

# Properties modified on dLUTColorBar
dLUTColorBar.HorizontalTitle = 1

# Properties modified on dLUTColorBar
dLUTColorBar.WindowLocation = 'LowerLeftCorner'

# Properties modified on dLUTColorBar
dLUTColorBar.WindowLocation = 'LowerRightCorner'

# Properties modified on dLUTColorBar
dLUTColorBar.RangeLabelFormat = '%-#6.1f'

# Properties modified on dLUTColorBar
dLUTColorBar.DrawTickLabels = 0

# Properties modified on dLUTColorBar
dLUTColorBar.ScalarBarThickness = ScalarBarThickness
dLUTColorBar.ScalarBarLength = ScalarBarLength

# Rescale transfer function
dLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
dPWF.RescaleTransferFunction(0.0, 1.0)

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'RealStress'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(dLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
calculator2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
realStressLUT.ApplyPreset('jet', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
realStressLUT.ApplyPreset('jet', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
realStressLUT.ApplyPreset('jet', True)

# get color legend/bar for realStressLUT in view renderView1
realStressLUTColorBar = GetScalarBar(realStressLUT, renderView1)
realStressLUTColorBar.Title = 'RealStress'
realStressLUTColorBar.ComponentTitle = ''
realStressLUTColorBar.TitleFontFile = ''
realStressLUTColorBar.LabelFontFile = ''

# Properties modified on realStressLUTColorBar
realStressLUTColorBar.Title = '$\\sigma_{sp1}$'
realStressLUTColorBar.HorizontalTitle = 1
realStressLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
realStressLUTColorBar.TitleFontFamily = 'Times'
realStressLUTColorBar.TitleFontSize = TitleFontSize
realStressLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
realStressLUTColorBar.LabelFontFamily = 'Times'
realStressLUTColorBar.LabelFontSize = LabelFontSize

# Properties modified on realStressLUTColorBar
realStressLUTColorBar.WindowLocation = 'LowerCenter'

# Properties modified on realStressLUTColorBar
realStressLUTColorBar.WindowLocation = 'LowerLeftCorner'

# Properties modified on realStressLUTColorBar
realStressLUTColorBar.WindowLocation = 'LowerRightCorner'

# Properties modified on realStressLUTColorBar
realStressLUTColorBar.RangeLabelFormat = '%-#6.2f'

# Properties modified on realStressLUTColorBar
realStressLUTColorBar.DrawTickLabels = 0

# Properties modified on realStressLUTColorBar
realStressLUTColorBar.ScalarBarThickness = ScalarBarThickness
realStressLUTColorBar.ScalarBarLength = ScalarBarLength

# Properties modified on animationScene1
animationScene1.PlayMode = 'Real Time'

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

lasttime=float(animationScene1.EndTime)
timelist=np.arange(0.5,lasttime,0.5)
if timelist[-1]<lasttime: timelist=np.append(timelist,lasttime)

for time in timelist:	
	# Properties modified on animationScene1
	animationScene1.AnimationTime = float(time)
	#################################################
	### For concentration
	#################################################
	# set scalar coloring
	ColorBy(calculator2Display, ('POINTS', 'c'))
	# Hide the scalar bar for this color map if no visible data is colored by it.
	HideScalarBarIfNotNeeded(realStressLUT, renderView1)
	HideScalarBarIfNotNeeded(dLUT, renderView1)
	# rescale color and/or opacity maps used to include current data range
	calculator2Display.RescaleTransferFunctionToDataRange(True, False)
	# show color bar/color legend
	calculator2Display.SetScalarBarVisibility(renderView1, True)

	# rescale color and/or opacity maps used to exactly fit the current data range
	calculator2Display.RescaleTransferFunctionToDataRange(False, True)

	# Properties modified on cLUTColorBar
	cLUTColorBar.RangeLabelFormat = '%-#6.2f'

	# rescale color and/or opacity maps used to exactly fit the current data range
	calculator2Display.RescaleTransferFunctionToDataRange(False, True)
	# current camera placement for renderView1
	renderView1.InteractionMode = '2D'
	renderView1.CameraPosition = [CameraX,CameraY, 10000.0]
	renderView1.CameraFocalPoint = [CameraX,CameraY, 0.0]
	renderView1.CameraParallelScale = CameraScale
	# save screenshot
	filename=currentdir+'/'+prefix+'c-%.1f.jpeg'%(time)
	SaveScreenshot(filename,renderView1,ImageResolution=[1105, 954], 
    # JPEG options
    Quality=100)

    #################################################
	### For concentration
	#################################################
    # set scalar coloring
	ColorBy(calculator2Display, ('POINTS', 'd'))
	# Hide the scalar bar for this color map if no visible data is colored by it.
	HideScalarBarIfNotNeeded(realStressLUT, renderView1)
	HideScalarBarIfNotNeeded(cLUT, renderView1)
	# rescale color and/or opacity maps used to include current data range
	calculator2Display.RescaleTransferFunctionToDataRange(True, False)
	# show color bar/color legend
	calculator2Display.SetScalarBarVisibility(renderView1, True)
	# rescale color and/or opacity maps used to exactly fit the current data range
	calculator2Display.RescaleTransferFunctionToDataRange(False, True)
	# Rescale transfer function
	dLUT.RescaleTransferFunction(0.0, 1.0)
	# Rescale transfer function
	dPWF.RescaleTransferFunction(0.0, 1.0)
	# current camera placement for renderView1
	renderView1.InteractionMode = '2D'
	renderView1.CameraPosition = [CameraX,CameraY, 10000.0]
	renderView1.CameraFocalPoint = [CameraX,CameraY, 0.0]
	renderView1.CameraParallelScale = CameraScale
	# save screenshot
	filename=currentdir+'/'+prefix+'d-%.1f.jpeg'%(time)
	SaveScreenshot(filename, renderView1, ImageResolution=[1105, 954], 
    # JPEG options
    Quality=100)
    #################################################
	### For stress
	#################################################
	# set scalar coloring
	ColorBy(calculator2Display, ('POINTS', 'RealStress'))
	# Hide the scalar bar for this color map if no visible data is colored by it.
	HideScalarBarIfNotNeeded(dLUT, renderView1)
	HideScalarBarIfNotNeeded(cLUT, renderView1)
	# rescale color and/or opacity maps used to include current data range
	calculator2Display.RescaleTransferFunctionToDataRange(True, False)
	# show color bar/color legend
	calculator2Display.SetScalarBarVisibility(renderView1, True)
	# rescale color and/or opacity maps used to exactly fit the current data range
	calculator2Display.RescaleTransferFunctionToDataRange(False, True)
	# Properties modified on realStressLUTColorBar
	realStressLUTColorBar.RangeLabelFormat = '%-#7.2f'
	# rescale color and/or opacity maps used to exactly fit the current data range
	calculator2Display.RescaleTransferFunctionToDataRange(False, True)
	# current camera placement for renderView1
	renderView1.InteractionMode = '2D'
	renderView1.CameraPosition = [CameraX,CameraY, 10000.0]
	renderView1.CameraFocalPoint = [CameraX,CameraY, 0.0]
	renderView1.CameraParallelScale = CameraScale
	# save screenshot
	filename=currentdir+'/'+prefix+'stress-%.1f.jpeg'%(time)
	SaveScreenshot(filename, renderView1, ImageResolution=[1105, 954], 
    # JPEG options
    Quality=100)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [CameraX,CameraY, 10000.0]
renderView1.CameraFocalPoint = [CameraX,CameraY, 0.0]
renderView1.CameraParallelScale = CameraScale

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
print('*** last time=%.2f'%(lasttime))
print('*** Job finished!')