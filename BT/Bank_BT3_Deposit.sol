// which we write the smart contract 
pragma solidity 0.6.0; 
    
// Creating a contract 
contract wallet{ 
 
          address payable public Owner; 
 
 // mapping is created for mapping 
 // address=>uint for transaction 
mapping(address=>uint) Amount; 
  
 // Defining a constructor 
 constructor() public payable{ 
 // msg.sender is the address of the 
 // person who has currently deployed contract 
  Owner = msg.sender 
           Amount[Owner] = msg.value; 
  } 
                  modifier onlyOwner(){ 
  require(Owner == msg.sender); 
 } 
 
function sendMoney (address payable receiver, uint amount) 
 public payable onlyOwner 
          { 
  require( receiver.balance>0); 
  require(amount>0); 
  Amount[Owner] -= amount; 
  Amount[receiver] += amount; 
 } 
 function ReceiveMoney() public payable{ 
 } 
 
 function CheckBalance_contractAccount() 
 public view onlyOwner returns(uint){ 
  return address(this).balance; 
 } 
function CheckBalance() 
 public view onlyOwner returns(uint){ 
  return Amount[Owner]; 
} 
}