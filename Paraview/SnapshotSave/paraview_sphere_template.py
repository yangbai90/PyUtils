# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'ExodusIIReader'
sphere20_outee = ExodusIIReader(FileName=['/home/by/MyCluster/Calc/Moose/LIBsV2/DisIntegration/Paper/SphereR8New1/Models/NewSim/Flux/GBs_5C/20/sphere20_oute.e'])
sphere20_outee.ElementVariables = []
sphere20_outee.PointVariables = []
sphere20_outee.GlobalVariables = []
sphere20_outee.NodeSetArrayStatus = []
sphere20_outee.SideSetArrayStatus = []

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on sphere20_outee
sphere20_outee.ElementVariables = ['Damage', 'HyStress', 'J_', 'MaxPrinStress', 'MinPrinStress', 'TractionLocal_', 'vonMises']
sphere20_outee.PointVariables = ['Damage', 'HyStress', 'J_', 'MaxPrinStress', 'MinPrinStress', 'TractionLocal_', 'c', 'disp_', 'mu', 'vonMises']
sphere20_outee.GlobalVariables = ['Damage', 'Damage0', 'DamageN', 'DamageT', 'MaxPrin', 'MinPrin', 'cs', 'soc', 'vonMises']
sphere20_outee.ElementBlocks = ['Unnamed block ID: 1 Type: TETRA4', 'Unnamed block ID: 2 Type: TETRA4', 'Unnamed block ID: 3 Type: TETRA4', 'Unnamed block ID: 4 Type: TETRA4', 'Unnamed block ID: 5 Type: TETRA4', 'Unnamed block ID: 6 Type: TETRA4', 'Unnamed block ID: 7 Type: TETRA4', 'Unnamed block ID: 8 Type: TETRA4', 'Unnamed block ID: 9 Type: TETRA4', 'Unnamed block ID: 10 Type: TETRA4', 'Unnamed block ID: 11 Type: TETRA4', 'Unnamed block ID: 12 Type: TETRA4', 'Unnamed block ID: 13 Type: TETRA4', 'Unnamed block ID: 14 Type: TETRA4', 'Unnamed block ID: 15 Type: TETRA4', 'Unnamed block ID: 16 Type: TETRA4', 'Unnamed block ID: 17 Type: TETRA4', 'Unnamed block ID: 18 Type: TETRA4', 'Unnamed block ID: 19 Type: TETRA4', 'Unnamed block ID: 20 Type: TETRA4']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1300, 954]

# show data in view
sphere20_outeeDisplay = Show(sphere20_outee, renderView1)

# trace defaults for the display properties.
sphere20_outeeDisplay.Representation = 'Surface'
sphere20_outeeDisplay.ColorArrayName = [None, '']
sphere20_outeeDisplay.OSPRayScaleArray = 'Damage'
sphere20_outeeDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sphere20_outeeDisplay.SelectOrientationVectors = 'Damage'
sphere20_outeeDisplay.ScaleFactor = 1.6416793793439866
sphere20_outeeDisplay.SelectScaleArray = 'Damage'
sphere20_outeeDisplay.GlyphType = 'Arrow'
sphere20_outeeDisplay.GlyphTableIndexArray = 'Damage'
sphere20_outeeDisplay.GaussianRadius = 0.08208396896719933
sphere20_outeeDisplay.SetScaleArray = ['POINTS', 'Damage']
sphere20_outeeDisplay.ScaleTransferFunction = 'PiecewiseFunction'
sphere20_outeeDisplay.OpacityArray = ['POINTS', 'Damage']
sphere20_outeeDisplay.OpacityTransferFunction = 'PiecewiseFunction'
sphere20_outeeDisplay.DataAxesGrid = 'GridAxesRepresentation'
sphere20_outeeDisplay.SelectionCellLabelFontFile = ''
sphere20_outeeDisplay.SelectionPointLabelFontFile = ''
sphere20_outeeDisplay.PolarAxes = 'PolarAxesRepresentation'
sphere20_outeeDisplay.ScalarOpacityUnitDistance = 0.7957073064546666

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
sphere20_outeeDisplay.DataAxesGrid.XTitleFontFile = ''
sphere20_outeeDisplay.DataAxesGrid.YTitleFontFile = ''
sphere20_outeeDisplay.DataAxesGrid.ZTitleFontFile = ''
sphere20_outeeDisplay.DataAxesGrid.XLabelFontFile = ''
sphere20_outeeDisplay.DataAxesGrid.YLabelFontFile = ''
sphere20_outeeDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
sphere20_outeeDisplay.PolarAxes.PolarAxisTitleFontFile = ''
sphere20_outeeDisplay.PolarAxes.PolarAxisLabelFontFile = ''
sphere20_outeeDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
sphere20_outeeDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(sphere20_outeeDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
sphere20_outeeDisplay.SetScalarBarVisibility(renderView1, True)

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

# Properties modified on sphere20_outee
sphere20_outee.DisplacementMagnitude = 10.0

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToLast()

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]

# create a new 'Calculator'
calculator1 = Calculator(Input=sphere20_outee)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'RealStress'
calculator1.Function = 'MaxPrinStress*87.17'

# show data in view
calculator1Display = Show(calculator1, renderView1)

# get color transfer function/color map for 'RealStress'
realStressLUT = GetColorTransferFunction('RealStress')
realStressLUT.RGBPoints = [-98.85140870365426, 0.231373, 0.298039, 0.752941, 151.39418745521044, 0.865003, 0.865003, 0.865003, 401.63978361407516, 0.705882, 0.0156863, 0.14902]
realStressLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RealStress'
realStressPWF = GetOpacityTransferFunction('RealStress')
realStressPWF.Points = [-98.85140870365426, 0.0, 0.5, 0.0, 401.63978361407516, 1.0, 0.5, 0.0]
realStressPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'RealStress']
calculator1Display.LookupTable = realStressLUT
calculator1Display.OSPRayScaleArray = 'RealStress'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'Damage'
calculator1Display.ScaleFactor = 2.1944704055786133
calculator1Display.SelectScaleArray = 'RealStress'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'RealStress'
calculator1Display.GaussianRadius = 0.10972352027893066
calculator1Display.SetScaleArray = ['POINTS', 'RealStress']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'RealStress']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.SelectionCellLabelFontFile = ''
calculator1Display.SelectionPointLabelFontFile = ''
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = realStressPWF
calculator1Display.ScalarOpacityUnitDistance = 1.0542771522049337

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
Hide(sphere20_outee, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(sphere20_outee)

# set active source
SetActiveSource(calculator1)

# create a new 'Calculator'
calculator2 = Calculator(Input=calculator1)
calculator2.Function = ''

# Properties modified on calculator2
calculator2.ResultArrayName = 'd'
calculator2.Function = 'Damage*1.2'

# show data in view
calculator2Display = Show(calculator2, renderView1)

# get color transfer function/color map for 'd'
dLUT = GetColorTransferFunction('d')
dLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.6, 0.865003, 0.865003, 0.865003, 1.2, 0.705882, 0.0156863, 0.14902]
dLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'd'
dPWF = GetOpacityTransferFunction('d')
dPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.2, 1.0, 0.5, 0.0]
dPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['POINTS', 'd']
calculator2Display.LookupTable = dLUT
calculator2Display.OSPRayScaleArray = 'd'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'Damage'
calculator2Display.ScaleFactor = 2.1944704055786133
calculator2Display.SelectScaleArray = 'd'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'd'
calculator2Display.GaussianRadius = 0.10972352027893066
calculator2Display.SetScaleArray = ['POINTS', 'd']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'd']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.SelectionCellLabelFontFile = ''
calculator2Display.SelectionPointLabelFontFile = ''
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityFunction = dPWF
calculator2Display.ScalarOpacityUnitDistance = 1.0542771522049337

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

# create a new 'Clip'
clip1 = Clip(Input=calculator2)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'd']
clip1.Value = 0.6

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [8.55199909210205, 7.696143984794617, 8.03603446483612]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'd']
clip1Display.LookupTable = dLUT
clip1Display.OSPRayScaleArray = 'd'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'Damage'
clip1Display.ScaleFactor = 2.183151459693909
clip1Display.SelectScaleArray = 'd'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'd'
clip1Display.GaussianRadius = 0.10915757298469543
clip1Display.SetScaleArray = ['POINTS', 'd']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'd']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = dPWF
clip1Display.ScalarOpacityUnitDistance = 1.08426359698167

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(calculator2)

# create a new 'Clip'
clip2 = Clip(Input=calculator2)
clip2.ClipType = 'Plane'
clip2.Scalars = ['POINTS', 'd']
clip2.Value = 0.6

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [8.55199909210205, 7.696143984794617, 8.03603446483612]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2.ClipType)

# Properties modified on clip2.ClipType
clip2.ClipType.Normal = [0.0, 1.0, 0.0]

# Properties modified on clip2.ClipType
clip2.ClipType.Normal = [0.0, 1.0, 0.0]

# show data in view
clip2Display = Show(clip2, renderView1)

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = ['POINTS', 'd']
clip2Display.LookupTable = dLUT
clip2Display.OSPRayScaleArray = 'd'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'Damage'
clip2Display.ScaleFactor = 2.1935792207717895
clip2Display.SelectScaleArray = 'd'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'd'
clip2Display.GaussianRadius = 0.10967896103858948
clip2Display.SetScaleArray = ['POINTS', 'd']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = ['POINTS', 'd']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.SelectionCellLabelFontFile = ''
clip2Display.SelectionPointLabelFontFile = ''
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityFunction = dPWF
clip2Display.ScalarOpacityUnitDistance = 1.1219325926274508

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip2Display.DataAxesGrid.XTitleFontFile = ''
clip2Display.DataAxesGrid.YTitleFontFile = ''
clip2Display.DataAxesGrid.ZTitleFontFile = ''
clip2Display.DataAxesGrid.XLabelFontFile = ''
clip2Display.DataAxesGrid.YLabelFontFile = ''
clip2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip2Display.PolarAxes.PolarAxisTitleFontFile = ''
clip2Display.PolarAxes.PolarAxisLabelFontFile = ''
clip2Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(clip2Display, ('POINTS', 'c'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(dLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'c'
cLUT = GetColorTransferFunction('c')
cLUT.RGBPoints = [0.4011473322394092, 0.231373, 0.298039, 0.752941, 0.7026139486476273, 0.865003, 0.865003, 0.865003, 1.0040805650558455, 0.705882, 0.0156863, 0.14902]
cLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'c'
cPWF = GetOpacityTransferFunction('c')
cPWF.Points = [0.4011473322394092, 0.0, 0.5, 0.0, 1.0040805650558455, 1.0, 0.5, 0.0]
cPWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(clip1)

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'c'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(dLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for cLUT in view renderView1
cLUTColorBar = GetScalarBar(cLUT, renderView1)
cLUTColorBar.WindowLocation = 'UpperRightCorner'
cLUTColorBar.Title = 'c'
cLUTColorBar.ComponentTitle = ''
cLUTColorBar.TitleFontFile = ''
cLUTColorBar.LabelFontFile = ''

# Properties modified on cLUTColorBar
cLUTColorBar.WindowLocation = 'LowerLeftCorner'
cLUTColorBar.Title = '$C/C_{max}$'
cLUTColorBar.HorizontalTitle = 1
cLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
cLUTColorBar.TitleFontFamily = 'Times'
cLUTColorBar.TitleFontSize = 25
cLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
cLUTColorBar.LabelFontFamily = 'Times'
cLUTColorBar.LabelFontSize = 20
cLUTColorBar.RangeLabelFormat = '%-#6.2f'

# Properties modified on cLUTColorBar
cLUTColorBar.WindowLocation = 'LowerRightCorner'

# Properties modified on cLUTColorBar
cLUTColorBar.DrawTickLabels = 0

# Properties modified on cLUTColorBar
cLUTColorBar.ScalarBarThickness = 35
cLUTColorBar.ScalarBarLength = 0.35

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
cLUT.ApplyPreset('jet', True)

# set active source
SetActiveSource(clip2)

# set active source
SetActiveSource(clip1)

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'd'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(cLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for dLUT in view renderView1
dLUTColorBar = GetScalarBar(dLUT, renderView1)
dLUTColorBar.WindowLocation = 'UpperRightCorner'
dLUTColorBar.Title = 'd'
dLUTColorBar.ComponentTitle = ''
dLUTColorBar.TitleFontFile = ''
dLUTColorBar.LabelFontFile = ''

# Properties modified on dLUTColorBar
dLUTColorBar.HorizontalTitle = 1
dLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
dLUTColorBar.TitleFontFamily = 'Times'
dLUTColorBar.TitleFontSize = 25
dLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
dLUTColorBar.LabelFontFamily = 'Times'
dLUTColorBar.LabelFontSize = 20
dLUTColorBar.RangeLabelFormat = '%-#6.1f'

# Properties modified on dLUTColorBar
dLUTColorBar.ScalarBarThickness = 35
dLUTColorBar.ScalarBarLength = 0.35

# Properties modified on dLUTColorBar
dLUTColorBar.WindowLocation = 'LowerRightCorner'

# set active source
SetActiveSource(clip2)

# set scalar coloring
ColorBy(clip2Display, ('POINTS', 'd'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(cLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
dLUT.ApplyPreset('Rainbow Uniform', True)

# set scalar coloring
ColorBy(clip2Display, ('POINTS', 'RealStress'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(dLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(clip1)

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'RealStress'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(dLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# get color legend/bar for realStressLUT in view renderView1
realStressLUTColorBar = GetScalarBar(realStressLUT, renderView1)
realStressLUTColorBar.WindowLocation = 'UpperRightCorner'
realStressLUTColorBar.Title = 'RealStress'
realStressLUTColorBar.ComponentTitle = ''
realStressLUTColorBar.TitleFontFile = ''
realStressLUTColorBar.LabelFontFile = ''

# Properties modified on realStressLUTColorBar
realStressLUTColorBar.WindowLocation = 'LowerRightCorner'
realStressLUTColorBar.Title = '$\\sigma_{sp1}$'
realStressLUTColorBar.HorizontalTitle = 1
realStressLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
realStressLUTColorBar.TitleFontFamily = 'Times'
realStressLUTColorBar.TitleFontSize = 25
realStressLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
realStressLUTColorBar.LabelFontFamily = 'Times'
realStressLUTColorBar.LabelFontSize = 20
realStressLUTColorBar.RangeLabelFormat = '%-#6.2f'

# Properties modified on realStressLUTColorBar
realStressLUTColorBar.ScalarBarThickness = 25
realStressLUTColorBar.ScalarBarLength = 0.35

# Properties modified on realStressLUTColorBar
realStressLUTColorBar.DrawTickLabels = 0

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
realStressLUT.ApplyPreset('jet', True)

# Properties modified on animationScene1
animationScene1.PlayMode = 'Real Time'

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'c'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(realStressLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(clip2)

# set scalar coloring
ColorBy(clip2Display, ('POINTS', 'c'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(realStressLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on cLUTColorBar
cLUTColorBar.WindowLocation = 'LowerLeftCorner'

# Properties modified on cLUTColorBar
cLUTColorBar.WindowLocation = 'LowerRightCorner'

# rescale color and/or opacity maps used to exactly fit the current data range
clip2Display.RescaleTransferFunctionToDataRange(False, True)

# set active source
SetActiveSource(clip1)

# rescale color and/or opacity maps used to exactly fit the current data range
clip1Display.RescaleTransferFunctionToDataRange(False, True)

# current camera placement for renderView1
renderView1.CameraPosition = [20.37263404268375, 42.11134010945224, 29.311567752908317]
renderView1.CameraFocalPoint = [2.8691353678433598, -2.274695191489951, 2.1437094593145045]
renderView1.CameraViewUp = [0.025980023901155558, -0.5293091059959553, 0.8480311955747017]
renderView1.CameraParallelScale = 14.210521176057018

# save screenshot
SaveScreenshot('/home/by/MyCluster/Calc/Moose/LIBsV2/DisIntegration/Paper/SphereR8New1/Models/NewSim/Flux/GBs_5C/20/c-t1.jpeg', renderView1, ImageResolution=[1297, 954], 
    # JPEG options
    Quality=100)

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'd'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(cLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(clip2)

# set scalar coloring
ColorBy(clip2Display, ('POINTS', 'd'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(cLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on dLUTColorBar
dLUTColorBar.WindowLocation = 'LowerRightCorner'

# rescale color and/or opacity maps used to exactly fit the current data range
clip2Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
dLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
dPWF.RescaleTransferFunction(0.0, 1.0)

# set active source
SetActiveSource(clip1)

# current camera placement for renderView1
renderView1.CameraPosition = [20.37263404268375, 42.11134010945224, 29.311567752908317]
renderView1.CameraFocalPoint = [2.8691353678433598, -2.274695191489951, 2.1437094593145045]
renderView1.CameraViewUp = [0.025980023901155558, -0.5293091059959553, 0.8480311955747017]
renderView1.CameraParallelScale = 14.210521176057018

# save screenshot
SaveScreenshot('/home/by/MyCluster/Calc/Moose/LIBsV2/DisIntegration/Paper/SphereR8New1/Models/NewSim/Flux/GBs_5C/20/d-t1.jpeg', renderView1, ImageResolution=[1297, 954], 
    # JPEG options
    Quality=100)

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'RealStress'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(dLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(clip2)

# set scalar coloring
ColorBy(clip2Display, ('POINTS', 'RealStress'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(dLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on realStressLUTColorBar
realStressLUTColorBar.WindowLocation = 'LowerRightCorner'

# rescale color and/or opacity maps used to exactly fit the current data range
clip2Display.RescaleTransferFunctionToDataRange(False, True)

# set active source
SetActiveSource(clip1)

# rescale color and/or opacity maps used to exactly fit the current data range
clip1Display.RescaleTransferFunctionToDataRange(False, True)

# current camera placement for renderView1
renderView1.CameraPosition = [20.37263404268375, 42.11134010945224, 29.311567752908317]
renderView1.CameraFocalPoint = [2.8691353678433598, -2.274695191489951, 2.1437094593145045]
renderView1.CameraViewUp = [0.025980023901155558, -0.5293091059959553, 0.8480311955747017]
renderView1.CameraParallelScale = 14.210521176057018

# save screenshot
SaveScreenshot('/home/by/MyCluster/Calc/Moose/LIBsV2/DisIntegration/Paper/SphereR8New1/Models/NewSim/Flux/GBs_5C/20/stress-t1.jpeg', renderView1, ImageResolution=[1297, 954], 
    # JPEG options
    Quality=100)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [20.37263404268375, 42.11134010945224, 29.311567752908317]
renderView1.CameraFocalPoint = [2.8691353678433598, -2.274695191489951, 2.1437094593145045]
renderView1.CameraViewUp = [0.025980023901155558, -0.5293091059959553, 0.8480311955747017]
renderView1.CameraParallelScale = 14.210521176057018

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).