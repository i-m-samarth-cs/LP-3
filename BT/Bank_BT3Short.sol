// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CustomerBank {
    
    mapping(address => uint256) public balanceOf;

    function deposit() public payable {
        balanceOf[msg.sender] += msg.value;
    }

    function withdraw(uint256 _amount) public {
        require(_amount <= balanceOf[msg.sender], "Not enough funds in account.");
        
        balanceOf[msg.sender] -= _amount;
        
        (bool success, ) = payable(msg.sender).call{value: _amount}("");
        require(success, "Ether transfer failed.");
    }
    
    function showBalance() public view returns (uint256) {
        return balanceOf[msg.sender];
    }
}