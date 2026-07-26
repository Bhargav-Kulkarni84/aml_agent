class EDATool:

    def run(self, context):

        df = context["data"]

        context["eda"] = {
            "rows": len(df),
            "missing": df.isnull().sum().to_dict(),
            "duplicates": df.duplicated().sum(),
            "class_distribution": df["is_laundering"].value_counts().to_dict()
        }

        return context