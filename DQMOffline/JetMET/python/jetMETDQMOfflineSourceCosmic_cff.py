import FWCore.ParameterSet.Config as cms

from DQMOffline.JetMET.jetMETAnalyzerCosmic_cff import *
from DQMOffline.JetMET.caloTowers_cff           import *
from DQMOffline.JetMET.BeamHaloAnalyzer_cfi     import *
AnalyzeBeamHalo.StandardDQM = cms.bool(True)

jetMETDQMOfflineSourceCosmic = cms.Sequence(analyzecaloTowersDQM*AnalyzeBeamHalo*jetMETAnalyzerCosmicSequence)
#jetMETDQMOfflineSourceCosmic = cms.Sequence(analyzecaloTowersDQM*jetMETAnalyzerCosmicSequence)
