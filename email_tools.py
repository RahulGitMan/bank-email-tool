class EmailTool:

    def execute(self, context):

        pdf = context["PDFTool"]

        return {
            "recipient": "treasury@demo-bank.com",
            "subject": "Daily Liquidity Report",
            "attachment": pdf["pdf_path"],
            "status": "Email Prepared"
        }