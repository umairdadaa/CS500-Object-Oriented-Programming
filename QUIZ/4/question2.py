from abc import ABC, abstractmethod

class DataProcessorInterface(ABC):
    @abstractmethod
    def processData(self, ids: list[int], data: list[list[float]]) -> dict[int, float]:
        pass

class DataProcessor(DataProcessorInterface):
    def processData(self, ids: list[int], data: list[list[float]]) -> dict[int, float]:
        results: dict[int, float] = {}
        
        for i in range(len(data)):
            total = 0.0
            for j in range(len(data[i])):
                total += data[i][j]
            
            average = total / len(data[i])
            results[ids[i]] = average
        
        return results

class DataProcessor2:
    def processData(self, data: dict[int, list[float]]) -> dict[int, float]:
        results: dict[int, float] = {}
        
        for k, v in data.items():
            total = 0.0
            for j in range(len(v)):
                total += v[j]
            
            average = total / len(v)
            results[k] = average
        
        return results

class Adapter(DataProcessorInterface):
    def __init__(self, processor: DataProcessor2):
        self.processor = processor

    def processData(self, ids: list[int], data: list[list[float]]) -> dict[int, float]:
        data_dict = {ids[i]: data[i] for i in range(len(ids))}
        return self.processor.processData(data_dict)

class Factory:
    def getDataProcessor(self) -> DataProcessorInterface:
        return Adapter(DataProcessor2())

def main():
    processor: DataProcessorInterface = Factory().getDataProcessor()
    ids = [101, 102, 103]
    data = [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]
    resultList = processor.processData(ids, data)
    print(resultList)

if __name__ == "__main__":
    main()
