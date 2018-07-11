"Logging functions to ensure unified output accross tuners"
from termcolor import cprint

class Logger():
 
    def __init__(self, hypertuner):
        
        # store a reference to the current tuner
        self.hypertuner = hypertuner

    def tuner_name(self, name):
        "Report tuner used"
        cprint("-=[%s]=-" % name, 'magenta')

    def new_instance(self, instance, num_instances, remaining_budget):
        "Report the search of a new instance"
        msg = "New instance - Epoch Budget %s/%s Num Instances %s" % (
                remaining_budget, self.hypertuner.epoch_budget, num_instances)
        cprint(msg, 'yellow')
        cprint("|- num params: %s" % instance.model_size)

    def done(self):
        msg = "Hypertuning complete - result in %s" % self.hypertuner.local_dir
        cprint(msg, 'green')
    
    def error(self, msg):
        cprint(msg, 'red')