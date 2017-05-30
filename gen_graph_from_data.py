import random
from generator import generate_data

data = generate_data(5)


class Property:
    """Propery constructor."""

    def __init__(self, name):
        self.name = name


# Instantiation of property instances
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
    """ Subsystems constructor. """

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

attitude_and_orbit_control = SubSysType('attitude and orbit control',
                                        [slug,
                                         ontology,
                                         power,
                                         mass,
                                         cost,
                                         min_working_temp,
                                         max_working_temp])

# Mapping from subsystem name to their instances
sub_system_mapping = {
    "communication": communication,
    "propulsion": propulsion,
    "detector": detector,
    "primary power": primary_power,
    "backup power": backup_power,
    "thermal": thermal,
    "structure": structure,
    "command and data": command_and_data,
    "attitude and orbit control": attitude_and_orbit_control
}


class Resource:
    """ Resource constructor."""

    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_


# component_123 = Resource(name=123, type_=primary_power)


def gen_components():
    """ Generates a component list from given data. """
    component_list = []
    for resource in data:
        # print(resource['name'])
        component_list.append(Resource(
            name=resource['name'],
            type_=sub_system_mapping[resource['object']['category']]))
        # print(sub_system_mapping[resource['object']['category']].type_)
    return component_list


class Graph:
    """ Graph constructor."""

    def __init__(self, subject_, predicate_, object_):
        self.subject = subject_
        self.predicate = predicate_
        self.object = object_


def find_property_value(object_name, property_name):
    """ Finds a property in data object given object name and property_name"""
    result_obj = None
    for object_ in data:
        # print(object_['name'])
        if object_['name'] == object_name:
            result_obj = object_
            break
    try:
        value = result_obj['object'][property_name]
    except:
        value = None

    return value


def gen_graph_data(component_list):
    """ Generates a list of Graph instances from a list of components. """
    component_list = gen_components()
    graph_data = []
    for component in component_list:
        for attribute in component.type_.allowed_properties:
            # print(component.name, attribute.name)
            graph_data.append(Graph(component, attribute, find_property_value(
                component.name, attribute.name)))
    return graph_data


component_list = gen_components()
graph_data = gen_graph_data(component_list)
# print(graph_data)

for graph_object in graph_data:
    print(graph_object.subject.name,
          graph_object.predicate.name, graph_object.object)
