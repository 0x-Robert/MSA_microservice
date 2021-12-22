/*
Run 컴포넌트는 div 태그에 {this.props.title} , ({this.props.type})을 갖고 있으며, Run 인스턴스의 props 속성을 통해 렌더링된다.

props 배열은 render() 함수에서 Run 인스턴스가 생성될 떄 채워진다.

*/

var Run = React.createClass({


    render: function(){
        return (
            <div>{this.props.title} ({this.props.type})</div>
        );
    }
});

var Runs = React.createClass({
    render: function(){
        var runNodes = this.props.data.map(function (run){
            return (
                <Run 
                    title={run.title}
                    type = {run.type}
                    />

            );
        });

        return (
            <div>
                {runNodes}
            </div>
        );
    }
});


