import random
#
# class Min_max_range:
#         """Defines a range class for for setting min - max ranges of different componenets"""
#     def __init__(self, min_val, max_val):
#         self.data = {"min":min_val, "max":max_val}

# Property instantiation
class Property:
    def __init__(self, name):
        self.name = name

slug = Property('slug')
ontology = Property('ontology')
power = Property('power')
mass = Property('mass')
cost = Property('cost')
min_working_temp = Property('minWorkingTemp')
max_working_temp = Property('maxWorkingTemp')
active = Property('active')
passive = Property('passive')
density = Property('density')


class SubSysType:
    def __init__(self, type_, allowed_properties):
        self.type_ = type_
        self.allowed_properties = allowed_properties

# Subsystems instantiation
communication = SubSysType('communication', [slug,
                                             ontology,
                                             power,
                                             mass,
                                             min_working_temp,
                                             max_working_temp])

propulsion = SubSysType('propulsion', [slug,
                                       ontology,
                                       power,
                                       mass,
                                       cost,
                                       min_working_temp,
                                       max_working_temp])

detector = SubSysType('detector', [slug,
                                   ontology,
                                   power,
                                   mass,
                                   cost,
                                   min_working_temp,
                                   max_working_temp])

primary_power = SubSysType('primary power', [slug,
                                             ontology,
                                             power,
                                             density,
                                             mass,
                                             cost,
                                             min_working_temp,
                                             max_working_temp])

backup_power = SubSysType('backup power', [slug,
                                           ontology,
                                           power,
                                           density,
                                           mass,
                                           cost,
                                           min_working_temp,
                                           max_working_temp])

thermal = SubSysType('thermal', [slug,
                                 ontology,
                                 power,
                                 mass,
                                 cost,
                                 min_working_temp,
                                 max_working_temp])

structure = SubSysType('structure', [slug,
                                     ontology,
                                     mass,
                                     cost,
                                     min_working_temp,
                                     max_working_temp])

command_and_data = SubSysType('command and data', [slug,
                                                   ontology,
                                                   power,
                                                   mass,
                                                   cost,
                                                   min_working_temp,
                                                   max_working_temp])

attitude_and_orbit_control = SubSysType('attitude and orbit control', [slug,
                                                                       ontology,
                                                                       power,
                                                                       mass,
                                                                       cost,
                                                                       min_working_temp,
                                                                       max_working_temp])

class Resource:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_

component_123 = Resource(name = 123, type_ = primary_power)


class Graph:
    def __init__(self, subject_, predicate_, object_):
        self.subject = subject_
        self.predicate = predicate_
        self.object = object_
graph_data = []
for attribute in component_123.type.allowed_properties:
    graph_data.append(Graph(component_123, attribute, random.random()))

# print(graph_data)
for graph in graph_data:
    print(graph.subject.name, graph.predicate.name, graph.object)
# In the end we should ahve the objects generated by the script in the Graph table.
