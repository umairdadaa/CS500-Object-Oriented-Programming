# LegacyRectangle class
class LegacyRectangle:
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.__height

# ModernShape class
class ModernShape:
    def __init__(self, area: float, perimeter: float) -> None:
        self.__area = area
        self.__perimeter = perimeter

    def get_area(self) -> float:
        return self.__area

    def get_perimeter(self) -> float:
        return self.__perimeter

# RectangleAdapter class
class RectangleAdapter(ModernShape):
    def __init__(self, legacy_rectangle: LegacyRectangle) -> None:
        # The LegacyRectangle is the adaptee here
        self.__legacy_rectangle = legacy_rectangle
        super().__init__(
            area=self.__legacy_rectangle.get_width() * self.__legacy_rectangle.get_height(),
            perimeter=2 * (self.__legacy_rectangle.get_width() + self.__legacy_rectangle.get_height())
        )

    def get_area(self) -> float:
        return self.__legacy_rectangle.get_width() * self.__legacy_rectangle.get_height()

    def get_perimeter(self) -> float:
        return 2 * (self.__legacy_rectangle.get_width() + self.__legacy_rectangle.get_height())

# ShapeAdapter class
class ShapeAdapter(LegacyRectangle):
    def __init__(self, modern_shape: ModernShape) -> None:
        # The ModernShape is the adaptee here
        self.__modern_shape = modern_shape
        width = self.__calculate_width()
        height = self.__calculate_height()
        super().__init__(width, height)

    def __calculate_width(self) -> float:
        # Simplified logic to get width
        return (self.__modern_shape.get_perimeter() / 4)

    def __calculate_height(self) -> float:
        # Simplified logic to get height
        return (self.__modern_shape.get_area() / (self.__modern_shape.get_perimeter() / 4))

# Example usage
def main():
    # Using RectangleAdapter to adapt LegacyRectangle to ModernShape
    legacy_rectangle = LegacyRectangle(5, 10)
    adapter1 = RectangleAdapter(legacy_rectangle)
    print("Area using RectangleAdapter:", adapter1.get_area())
    print("Perimeter using RectangleAdapter:", adapter1.get_perimeter())

    # Using ShapeAdapter to adapt ModernShape to LegacyRectangle
    modern_shape = ModernShape(50, 30)
    adapter2 = ShapeAdapter(modern_shape)
    print("Width using ShapeAdapter:", adapter2.get_width())
    print("Height using ShapeAdapter:", adapter2.get_height())

if __name__ == "__main__":
    main()
