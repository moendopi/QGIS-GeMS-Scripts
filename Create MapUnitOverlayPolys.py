"""
Model exported as python.
Name : MapUnitOverlayPolys Add Fields
Group : 
With QGIS : 32401
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class MapunitoverlaypolysAddFields(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('contactsandfaults', 'contacts_and_faults', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Mapunitoverlaypolys', 'MapUnitOverlayPolys', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue='TEMPORARY_OUTPUT'))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(9, model_feedback)
        results = {}
        outputs = {}

        # Polygonize
        alg_params = {
            'INPUT': parameters['contactsandfaults'],
            'KEEP_FIELDS': False,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Polygonize'] = processing.run('native:polygonize', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # FID
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'FID',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 0,  # Integer (32 bit)
            'INPUT': outputs['Polygonize']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Fid'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # MapUnit
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'MapUnit',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # Text (string)
            'INPUT': outputs['Fid']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Mapunit'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # IdentityConfidence
        alg_params = {
            'FIELD_LENGTH': 50,
            'FIELD_NAME': 'IdentityConfidence',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # Text (string)
            'INPUT': outputs['Mapunit']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Identityconfidence'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Label
        alg_params = {
            'FIELD_LENGTH': 50,
            'FIELD_NAME': 'Label',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # Text (string)
            'INPUT': outputs['Identityconfidence']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Label'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Symbol
        alg_params = {
            'FIELD_LENGTH': 254,
            'FIELD_NAME': 'Symbol',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # Text (string)
            'INPUT': outputs['Label']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Symbol'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}

        # DataSourceID
        alg_params = {
            'FIELD_LENGTH': 50,
            'FIELD_NAME': 'DataSourceID',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # Text (string)
            'INPUT': outputs['Symbol']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Datasourceid'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}

        # Notes
        alg_params = {
            'FIELD_LENGTH': 254,
            'FIELD_NAME': 'Notes',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # Text (string)
            'INPUT': outputs['Datasourceid']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Notes'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(8)
        if feedback.isCanceled():
            return {}

        # MapUnitOverlayPolys_ID
        alg_params = {
            'FIELD_LENGTH': 50,
            'FIELD_NAME': 'MapUnitOverlayPolys_ID',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # Text (string)
            'INPUT': outputs['Notes']['OUTPUT'],
            'OUTPUT': parameters['Mapunitoverlaypolys']
        }
        outputs['Mapunitoverlaypolys_id'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Mapunitoverlaypolys'] = outputs['Mapunitoverlaypolys_id']['OUTPUT']
        return results

    def name(self):
        return 'MapUnitOverlayPolys Add Fields'

    def displayName(self):
        return 'MapUnitOverlayPolys Add Fields'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return MapunitoverlaypolysAddFields()
