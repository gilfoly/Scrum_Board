pragma solidity ^0.5.0;

contract ScrumBoard{
    
    uint public StoryCount=0;

    struct Story{
        uint id;
        string name;
        address writer;
        uint status;
    }
    
    mapping(uint => Story) public stories;
    
    event StoryCreated(
        uint id,
        string name,
        address writer,
        uint status
        );
        
    event InEmergency(
        uint id,
        string name,
        address writer,
        uint status
        );

    event StatusUpdated(
        uint id,
        string name,
        address writer,
        uint status
        );
        
    event InTesting(
        uint id,
        string name,
        address writer,
        uint status
        );
        
    event Completed(
        uint id,
        string name,
        address writer,
        uint status
        );
        
    function createStory(string memory _name) public{
        require(bytes(_name).length>0);
        require(tx.origin == msg.sender);
        StoryCount++;
        stories[StoryCount] = Story(StoryCount,_name,msg.sender,1);
        emit StoryCreated(StoryCount,_name,msg.sender,1);
    }

    function emergency(uint _id) public {
        require(_id>0 && _id<=StoryCount);
        require(tx.origin == msg.sender);
        Story memory _story = stories[_id];
        if(_story.status == 1){
            _story.status = 2;
        }
        stories[_id] = _story;
        emit StoryCreated(StoryCount,_story.name,msg.sender,_story.status);
        
    }
    
    function updateStatus(uint _id) public {
        require(_id>0 && _id<=StoryCount);
        Story memory _story = stories[_id];
        if(_story.status != 5){
            if(_story.status==1){
                _story.status = _story.status+2;
            }
            else{
                _story.status++;
            }
        }
        stories[_id] = _story;
        emit Completed(StoryCount,_story.name,msg.sender,_story.status);
    }
    
}