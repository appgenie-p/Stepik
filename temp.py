import abc


class FormalParserInterface(metaclass=abc.ABCMeta):
    # @classmethod
    # def __subclasshook__(cls, subclass):
    #     return (
    #         hasattr(subclass, 'load_data_source')
    #         and callable(subclass.load_data_source)
    #         and hasattr(subclass, 'extract_text')
    #         and callable(subclass.extract_text)
    #     )

    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    @abc.abstractmethod
    def extract_text(self, full_file_path: str) -> dict:
        pass


class PdfParserNew(FormalParserInterface):
    """Extract text from a PDF."""

    def load_data_source(self, path: str, file_name: str) -> str:
        # Implementation of load_data_source() method
        return f"Loading PDF file {file_name} from path {path}"

    def extract_text(self, full_file_path: str) -> dict:
        # Implementation of extract_text() method
        return {"text": "Extracted text from PDF file"}


class EmlParserNew(FormalParserInterface):
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        # Implementation of load_data_source() method
        return f"Loading email file {file_name} from path {path}"

    def extract_texttT(self, full_file_path: str) -> dict:
        # Implementation of extract_text() method
        return {"text": "Extracted text from email file"}


class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""

    pass


pdf = PdfParserNew()
eml = EmlParserNew()

isinstance(pdf, FormalParserInterface)
issubclass(PdfParserNew, FormalParserInterface)
isinstance(eml, FormalParserInterface)
issubclass(EmlParserNew, FormalParserInterface)
