"""
Errors for the assessment app.
"""
import copy


class PeerAssessmentError(Exception):
    """Generic Peer Assessment Error

    Raised when an error occurs while processing a request related to the
    Peer Assessment Workflow.

    """
    pass


class PeerAssessmentRequestError(PeerAssessmentError):
    """Error indicating insufficient or incorrect parameters in the request.

    Raised when the request does not contain enough information, or incorrect
    information which does not allow the request to be processed.

    """

    def __init__(self, field_errors):
        Exception.__init__(self, repr(field_errors))
        self.field_errors = copy.deepcopy(field_errors)


class PeerAssessmentWorkflowError(PeerAssessmentError):
    """Error indicating a step in the workflow cannot be completed,

    Raised when the action taken cannot be completed in the workflow. This can
    occur based on parameters specific to the Submission, User, or Peer Scorers.

    """
    pass


class PeerAssessmentInternalError(PeerAssessmentError):
    """Error indicating an internal problem independent of API use.

    Raised when an internal error has occurred. This should be independent of
    the actions or parameters given to the API.

    """
    pass


class SelfAssessmentError(Exception):
    """Generic Self Assessment Error

    Raised when an error occurs while processing a request related to the
    Self Assessment Workflow.

    """
    pass


class SelfAssessmentRequestError(SelfAssessmentError):
    """
    There was a problem with the request for a self-assessment.
    """
    pass


class SelfAssessmentInternalError(SelfAssessmentError):
    """
    There was an internal problem while accessing the self-assessment api.
    """
    pass

