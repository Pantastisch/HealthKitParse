import xml.etree.ElementTree as ET
import zipfile

def main():
    systBloodPleasureData = HKP_Record('HKP_BloodPressureSystolic')
    diastBloodPleasureData = HKP_Record('HKP_BloodPressureDiastolic')

    pass

class HKP_Record:
    '''Class which is containing all relevant data for the given Apple Health Kit record type'''
    
    def __init__(self, recordType):
        super().__init__()
        self.__recordType__ = HKP_RecordType(recordType)

        self.RecordType = self.__recordType__.RecordType
        self.Unit = self.__recordType__.Unit
        self.Records = None

    @property
    def Records(self):
        return self.__records__

    @Records.setter
    def Records(self, dummy = None):
        export = zipfile.ZipFile('input/Export.zip').open('apple_health_export/Export.xml')
        tree = ET.parse(export)
        root = tree.getroot()

        records = list()

        for child in root:
            if (child.tag == 'Record'):
                if (child.attrib['type'] == self.__recordType__.HealthKitType):
                    date = child.attrib['startDate']
                    value = child.attrib['value']
                    records.append(HKP_RecordData(date, value))

        self.__records__ = records


class HKP_RecordType:
    '''Class which shall contain all relevant data about a special type'''

    __recordTypes__ = {
        'HKP_BloodPressureSystolic' : {
            'healthKitType' : 'HKQuantityTypeIdentifierBloodPressureSystolic',
            'unit' : 'mmHg'
        },
        'HKP_BloodPressureDiastolic' : {
            'healthKitType' : 'HKQuantityTypeIdentifierBloodPressureDiastolic',
            'unit' : 'mmHg'
        }
    }

    def __init__(self, recordType):
        super().__init__()
        self.RecordType = recordType

    @property
    def RecordType(self):
        return self.__recordType__

    @RecordType.setter
    def RecordType(self, recordType):
        if (recordType not in self.__recordTypes__):
            raise NotImplementedError
        else:
            self.__recordType__ = recordType

    @property
    def Unit(self):
        return self.__recordTypes__[self.__recordType__]['unit']

    @property
    def HealthKitType(self):
        return self.__recordTypes__[self.__recordType__]['healthKitType']


class HKP_RecordData:
    '''Class which is containing one datapoint of a Healthkit Record'''
    def __init__(self, date, value):
        super().__init__()
        self.Date = date
        self.Value = value


if __name__ == "__main__":
    main()