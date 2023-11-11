import starknet from 'starknet-library';

// Initialize Starknet and user
const starknetProvider = new starknet.StarknetProvider();
const userWallet = new starknet.UserWallet();

// ERC-20 token smart contract
const tokenContractAddress = '0x123456789abcdef';

// Function to check user's balance
async function checkBalance() {
    try {
        const balance = await starknetProvider.getBalance(userWallet.getAddress(), tokenContractAddress);
        console.log(`Your balance: ${balance}`);
    } catch (error) {
        console.error(`Error checking balance: ${error}`);
    }
}

// Function to send tokens
async function sendTokens(recipient, amount) {
    try {
        await starknetProvider.transferTokens(userWallet, tokenContractAddress, recipient, amount);
        console.log(`Tokens sent to ${recipient}`);
    } catch (error) {
        console.error(`Error sending tokens: ${error}`);
    }
}

// Function to track a transaction
function trackTransaction(txHash) {
    starknetProvider.waitForTransactionConfirmation(txHash)
        .then(() => {
            console.log(`Transaction ${txHash} confirmed.`);
        })
        .catch((error) => {
            console.error(`Error tracking transaction: ${error}`);
        });
}

// Example usage of functions
checkBalance();
sendTokens('0xrecipientaddress', 100);
trackTransaction('0xtxhash');
