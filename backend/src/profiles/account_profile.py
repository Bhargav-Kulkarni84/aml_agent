class AccountProfile:

    def __init__(
        self,
        account_id,
        total_sent=0.0,
        total_received=0.0,
        outgoing_transactions=0,
        incoming_transactions=0,
        last_transaction=None,
        unique_receivers=None,
        unique_senders=None,
    ):

        self.account_id = account_id
        self.total_sent = total_sent
        self.total_received = total_received

        self.outgoing_transactions = outgoing_transactions
        self.incoming_transactions = incoming_transactions

        self.last_transaction = last_transaction

        if unique_receivers is None:
            unique_receivers = set()

        if unique_senders is None:
            unique_senders = set()

        self.unique_receivers = unique_receivers
        self.unique_senders = unique_senders