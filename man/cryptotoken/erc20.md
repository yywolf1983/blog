

token name
function name() public view returns (string)

token 符号
function symbol() public view returns (string)

位数
function decimals() public view returns (uint8)

总量
function totalSupply() public view returns (uint256)

获取余额
function balanceOf(address _owner) public view returns (uint256 balance)

发送
function transfer(address _to, uint256 _value) public returns (bool success)

合约转移
function transferFrom(address _from, address _to, uint256 _value) public returns (bool success)

最高额度
function approve(address _spender, uint256 _value) public returns (bool success)

允许额度
function allowance(address _owner, address _spender) public view returns (uint256 remaining)


转移事件触发
event Transfer(address indexed _from, address indexed _to, uint256 _value)

转移成功触发
event Approval(address indexed _owner, address indexed _spender, uint256 _value)

ERC223 代币标砖
ERC827 令牌标准（ERC20 扩展） 草案

EIP-165 标准接口检测
EIP-173 合同所有权标准

/// @title ERC-173 Contract Ownership Standard
///  Note: the ERC-165 identifier for this interface is 0x7f5828d0
interface ERC173 /* is ERC165 */ {
    /// @dev This emits when ownership of a contract changes.    
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /// @notice Get the address of the owner    
    /// @return The address of the owner.
    function owner() view external returns(address);
	
    /// @notice Set the address of the new owner of the contract
    /// @dev Set _newOwner to address(0) to renounce any ownership.
    /// @param _newOwner The address of the new owner of the contract    
    function transferOwnership(address _newOwner) external;	
}

interface ERC165 {
    /// @notice Query if a contract implements an interface
    /// @param interfaceID The interface identifier, as specified in ERC-165
    /// @dev Interface identification is specified in ERC-165. This function
    ///  uses less than 30,000 gas.
    /// @return `true` if the contract implements `interfaceID` and
    ///  `interfaceID` is not 0xffffffff, `false` otherwise
    function supportsInterface(bytes4 interfaceID) external view returns (bool);
}