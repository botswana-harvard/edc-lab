from django.contrib import messages
from edc_label import JobResult, PrintersMixin, PrinterError


class LabPrintersMixin(PrintersMixin):

    label_cls = None
    job_result_cls = JobResult

    @property
    def printer(self):
        printer = self.lab_label_printer
        if not printer:
            messages.error(
                self.request,
                'Your "lab" label printer is not configured. '
                'See Edc Label in Administration.')
            raise PrinterError('lab_label_printer not set. Got None')
        return printer

    def print_labels(self, pks=None, request=None):
        """Returns a job_result object or None after printing.
        """
        zpl_data = b''
        try:
            printer = self.printer
        except PrinterError:
            printer = None
            job_id = None
            job_result = None
        else:
            for pk in pks:
                label = self.label_cls(
                    pk=pk, children_count=len(pks), request=request)
                zpl_data += label.render_as_zpl_data()
            job_id = printer.stream_print(zpl_data=zpl_data)
            job_result = self.job_result_cls(
                name=self.label_cls.label_template_name, copies=1, job_ids=[job_id],
                printer=printer)
        return job_result
