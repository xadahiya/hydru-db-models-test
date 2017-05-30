# Property instantiation
class Property:
    def __init__(self, name):
        self.name = name


manufacturer = Property('manufacturer')
function = Property('function')
subSystemType = Property('subSystemType')
isStandard = Property('isStandard')
hasVolume = Property('hasVolume')
hasMinAmpere = Property('hasMinAmpere')
hasMaxAmpere = Property('hasMaxAmpere')
hasMass = Property('hasMass')
minWorkingTemperature = Property('minWorkingTemperature')
maxWorkingTemperature = Property('maxWorkingTemperature')
hasPower = Property('hasPower')
hasSpecificImpulse = Property('hasSpecificImpulse')
holdsSensor = Property('holdsSensor')
hasMonetaryValue = Property('hasMonetaryValue')
hasWireInWith = Property('hasWireInWith')
hasWireOutWith = Property('hasWireOutWith')
typeOfPropellant = Property('typeOfPropellant')


class SubSysType:
    def __init__(self, type_, allowed_properties=[]):
        self.type_ = type_
        self.allowed_properties = allowed_properties


cubicMillimeters = SubSysType('cubicMillimeters', [hasVolume])
spacecraft_Detector = SubSysType('Spacecraft_Detector', [hasWireOutWith,
                                                         hasWireInWith,
                                                         maxWorkingTemperature,
                                                         minWorkingTemperature,
                                                         hasVolta])
spacecraft_Propulsion = SubSysType('Spacecraft_Propulsion', [hasSpecificImpulse,
                                                             maxWorkingTemperature,
                                                             minWorkingTemperature,
                                                             hasWireInWith])

spacecraft_PrimaryPower = SubSysType('Spacecraft_PrimaryPower', [maxWorkingTemperature,
                                                                 minWorkingTemperature,
                                                                 hasWireOutWith])

spacecraft_BackupPower = SubSysType('Spacecraft_BackupPower', [minWorkingTemperature,
                                                               maxWorkingTemperature,
                                                               hasWireOutWith,
                                                               hasWireInWith])

spacecraft_Thermal = SubSysType('Spacecraft_Thermal', [])

spacecraft_Thermal_PassiveDevice = SubSysType('Spacecraft_Thermal_PassiveDevice', [
    maxWorkingTemperature, minWorkingTemperature])

spacecraft_Thermal_ActiveDevice = SubSysType(
    'Spacecraft_Thermal_ActiveDevice', [hasWireInWith])

spacecraft_Structure = SubSysType(
    'Spacecraft_Structure', [maxWorkingTemperature, minWorkingTemperature])

spacecraft_CDH = SubSysType('Spacecraft_CDH', [minWorkingTemperature,
                                               maxWorkingTemperature,
                                               hasWireOutWith,
                                               hasWireInWith])

spacecraft_Communication = SubSysType('Spacecraft_Communication', [maxWorkingTemperature,
                                                                   minWorkingTemperature,
                                                                   hasWireOutWith,
                                                                   hasWireInWith])

spacecraft_AODCS = SubSysType('Spacecraft_AODCS', [
    minWorkingTemperature, maxWorkingTemperature, hasWireOutWith])

spacecraft_AODCS_Active = SubSysType('Spacecraft_AODCS_Active', hasWireInWith)

spacecraft_AODCS_PassiveDevice = SubSysType(
    'Spacecraft_AODCS_PassiveDevice', [hasWireInWith])
