# edc-lab
[![Build Status](https://travis-ci.org/clinicedc/edc-lab.svg?branch=develop)](https://travis-ci.org/clinicedc/edc-lab) [![Coverage Status](https://coveralls.io/repos/github/clinicedc/edc-lab/badge.svg?branch=develop)](https://coveralls.io/github/clinicedc/edc-lab?branch=develop)

Lab classes


### Installation


Get the latest version:

    pip install git+https://github.com/botswana-harvard/edc-lab@develop#egg=edc-lab

Add to settings:

    INSTALLED_APPS = [
        ...
        'edc_lab.apps.AppConfig',
        ...
    ]

### Configuration

Create aliquots configurations and their relationship:
    
    wb = AliquotType(name='whole_blood', alpha_code='WB', numeric_code='02')
    bc = AliquotType(name='buffy_coat', alpha_code='BC', numeric_code='16')
    pl = AliquotType(name='plasma', alpha_code='PL', numeric_code='32')
    
    wb.add_derivatives(pl, bc)
    
Set up one or more processing profiles:

    processing_profile = ProcessingProfile(
        name='viral_load', aliquot_type=wb)
    process_bc = Process(aliquot_type=bc, aliquot_count=4)
    process_pl = Process(aliquot_type=pl, aliquot_count=2)
    processing_profile.add_processes(process_bc, process_pl)
    
Create one or more panels:

    panel = RequisitionPanel(
        name='panel',
        aliquot_type=a,
        processing_profile=processing_profile)
    
Create a lab profile:

    lab_profile = LabProfile(name='lab_profile')
    lab_profile.add_panel(panel)
    
Register the `lab_profile` with site:

    site_labs.register(lab_profile, requisition_model='edc_lab.subjectrequisition')

### Usage

Create a requisition model instance:

    requisition = SubjectRequisition.objects.create(
        subject_visit=self.subject_visit,
        panel_name=self.panel.name,
        is_drawn=YES)

Pass the requisition to `Specimen`

    specimen = Specimen(requisition=requisition)

Process:
    
    specimen.process()
    
Aliquots have been created according to the configured processing profile:

    >>> specimen.primary_aliquot.identifier
    99900GV63F00000201
 
    >>> for aliquot in specimen.aliquots.order_by('count'):
           print(aliquot.aliquot_identifier)
    99900GV63F00000201
    99900GV63F02013202
    99900GV63F02013203
    99900GV63F02011604
    99900GV63F02011605
    99900GV63F02011606
    99900GV63F02011607
 
    
    
