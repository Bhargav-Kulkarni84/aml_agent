import pandas as pd

from profiles.profile_manager import ProfileManager


class TransactionProcessor:

    def __init__(self):
        self.profile_manager = ProfileManager()

    def process(self, df: pd.DataFrame):

        print("\nGenerating behavioral features...")

        feature_rows = []

        for row in df.itertuples(index=False):

            sender = self.profile_manager.get_profile(row.sender_account)
            receiver = self.profile_manager.get_profile(row.receiver_account)

            #Compute the time passed between previous and current transactions.
            if sender.last_transaction is None: seconds_since_last_tx = -1
            else: seconds_since_last_tx = (row.timestamp - sender.last_transaction).total_seconds()

            #Compute the average outgoing transaction amount.
            if sender.outgoing_transactions == 0 : avg_sent_amount = 0.0
            else:avg_sent_amount = (sender.total_sent / sender.outgoing_transactions)

            #Compute the amount to average ratio.
            if avg_sent_amount == 0:amount_to_avg_ratio = 1.0
            else:amount_to_avg_ratio = (row.amount /avg_sent_amount)

            #FAN OUT RATIO
            if sender.outgoing_transactions == 0:fan_out_ratio = 0.0
            else:fan_out_ratio = (len(sender.unique_receivers)/ sender.outgoing_transactions)

            #FAN IN RATIO
            if receiver.incoming_transactions == 0:fan_in_ratio = 0.0
            else:fan_in_ratio = (len(receiver.unique_senders)/ receiver.incoming_transactions)

            rapid_tx_flag = (seconds_since_last_tx != -1 and seconds_since_last_tx < 60)

            large_tx_flag = amount_to_avg_ratio > 5

            #Features before updating the sender and receiver.
            features = {

                "sender_account": row.sender_account,

                "receiver_account": row.receiver_account,

                "amount": row.amount,

                "timestamp": row.timestamp,

                "is_laundering": row.is_laundering,

                "laundering_type": row.laundering_type,

                # Behavioral features

                "seconds_since_last_tx": seconds_since_last_tx,

                "sender_avg_sent_amount": avg_sent_amount,

                "amount_to_avg_ratio": amount_to_avg_ratio,

                "sender_total_sent":sender.total_sent,

                "sender_total_received":sender.total_received,

                "sender_outgoing_transactions":sender.outgoing_transactions,

                "sender_incoming_transactions":sender.incoming_transactions,

                "sender_unique_receivers":len(sender.unique_receivers),

                "receiver_unique_senders":len(receiver.unique_senders),

                "sender_fan_out_ratio": fan_out_ratio,

                "receiver_fan_in_ratio": fan_in_ratio,

                "rapid_tx_flag": rapid_tx_flag,

                "large_tx_flag" : large_tx_flag

                
            } 

            #Update the sender transaction
            sender.total_sent += row.amount

            sender.outgoing_transactions += 1

            sender.unique_receivers.add(
                row.receiver_account
            )

            sender.last_transaction = row.timestamp

            #Update the receiver transaction
            receiver.total_received += row.amount

            receiver.incoming_transactions += 1

            receiver.unique_senders.add(
                row.sender_account
            )

            receiver.last_transaction = row.timestamp

            #Append the features before current update to features row
            feature_rows.append(features)

        return pd.DataFrame(feature_rows)