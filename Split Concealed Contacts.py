"""
Model exported as python.
Name : Split Concealed Contacts
Group : 
With QGIS : 32401
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class SplitConcealedContacts(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('contactsandfaults', 'ContactsAndFaults', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('surficiallines', 'Surficial_lines', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Contactsandfaults_split', 'ContactsAndFaults_Split', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Split with lines
        alg_params = {
            'INPUT': parameters['contactsandfaults'],
            'LINES': parameters['surficiallines'],
            'OUTPUT': parameters['Contactsandfaults_split']
        }
        outputs['SplitWithLines'] = processing.run('native:splitwithlines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Contactsandfaults_split'] = outputs['SplitWithLines']['OUTPUT']
        return results

    def name(self):
        return 'Split Concealed Contacts'

    def displayName(self):
        return 'Split Concealed Contacts'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return SplitConcealedContacts()
