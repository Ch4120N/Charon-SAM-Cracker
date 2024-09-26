import argparse


class CusHelpFormatter(argparse.HelpFormatter):
    """A custom HelpFormatter class that capitalizes the first letter of usage text."""
    def add_usage(self, usage, actions, groups, prefix=None):
        """Add usage method to display the usage text with the first letter capitalized."""
        if prefix is None:
            prefix = ''
        return super(CusHelpFormatter, self).add_usage(
            usage, actions, groups, prefix)