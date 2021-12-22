/*
Runnerly에서 달리기 정보는 다른 마이크로 서비스에 의해 만들어지므로, 또 다른 리액트 컴포넌트가 필요하다.
이 컴포넌트의 역활은 XMLHttpRequest 클래스로 AJAX(Asynchronous JavaScript and XML)를 사용해서 달리기 정보를 비동기로 로드하는 것이다.
이 동작을 구현한 코드가 다음 예제의 loadRunsFromServer()함수다. 이 함수는 props.url 속성에 GET 요청을 보내서 데이터를 가져온 후 setState()함수로 props.data 값을 업데이트 한다.

*/

var RunsBox = React.createClass({
    loadRunsFromServer: function(){
        var xhr = new XMLHttpRequest();
        xhr.open('get', this.props.url, true);
        xhr.withCredentials = true;
        xhr.onload = function(){
            var data  = JSON.parse(xhr.responseText);
            this.setState({data: data});

        }.bind(this);
        xhr.send();
    },

    getInitialState: function(){
        return {data: []};
    },

    componentDidMount:function(){
        this.loadRunsFromServer();
    },

    render: function(){
        return (
            <div>

                <h2>Runs</h2>
                <Runs data={this.state.data}/>

            </div>
        );
    }

});

/* RunsBox를 전역으로 노출한다. */
window.RunsBox = RunsBox; 

