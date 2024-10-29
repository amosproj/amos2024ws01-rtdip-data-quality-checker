# Copyright 2022 RTDIP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pyspark.sql.dataframe import DataFrame as PySparkDataFrame
from pyspark.sql.functions import desc


from rtdip_sdk.pipelines.monitoring.interfaces import MonitoringBaseInterface
from rtdip_sdk.pipelines._pipeline_utils.models import Libraries, SystemType


class DuplicateDetection(MonitoringBaseInterface):
    """
    Cleanses a PySpark DataFrame from duplicates.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.monitoring.spark.data_quality.duplicate_detection import DuplicateDetection
    from pyspark.sql import SparkSession
    from pyspark.sql.dataframe import DataFrame

    duplicate_detection_monitor = DuplicateDetection(df)

    result = duplicate_detection_monitor.filter()
    ```

    Parameters:
        df (DataFrame): PySpark DataFrame to be converted
    """

    df: PySparkDataFrame

    def __init__(self, df: PySparkDataFrame) -> None:
        self.df = df

    @staticmethod
    def system_type():
        """
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
        return SystemType.PYSPARK

    @staticmethod
    def libraries():
        libraries = Libraries()
        return libraries

    @staticmethod
    def settings() -> dict:
        return {}

    def filter(self) -> PySparkDataFrame:
        """
        Returns:
            DataFrame: A cleansed PySpark DataFrame from all the duplicates.
        """


        cleansed_df = self.df.dropDuplicates(['TagName', 'EventTime']).orderBy(desc("EventTime"))
        return cleansed_df