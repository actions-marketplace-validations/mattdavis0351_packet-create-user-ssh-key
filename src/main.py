import packet
import os

# Collect input variables from workflow
API_key = os.getenv("INPUT_API_KEY")
key_label = os.getenv("INPUT_KEY_LABEL")
public_key = os.getenv("INPUT_PUBLIC_KEY")


# Check if required inputs have been received
if API_key == "No key supplied" or public_key == "No key supplied":
    raise ValueError(
        f"Cannot supply empty value.\n Current API key is: %s\nCurrent public key is: %s" % (API_key, public_key))

# Create Packet.com API client
manager = packet.Manager(auth_token=API_key)

key = manager.create_ssh_key(label=key_label,
                             public_key=public_key)


# Set outputs for action
print(f"::set-output name=key_id::{key.id}")
print(f"::set-output name=key_owner::{key.owner}")


# Profit
