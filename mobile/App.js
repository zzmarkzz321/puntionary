import React, { Component, PropTypes } from 'react';
import { Animated, AppRegistry, Button, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

/**
* :D
* 
* States that you'll probably care about:
*   query - The string that the user inputs
*   results - The new string
**/

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      text: '',
      query: '',
      results: '',
      offsetY: new Animated.Value(0),
    };
  }

  render() {
    return (
        <View style={styles.container}>
          <Animated.View style={{transform: [{translateY: this.state.offsetY}]}}>
            <View style={styles.inputContainer}>
              <TextInput
                style={{height:40, textAlign:'center'}}
                placeholder="Enter a phrase or sentence"
                returnKeyLabel={"next"}
                onChangeText={(text) => this.setState({query:text})}
              />
            </View>

            <View style={styles.buttonContainer}>
              <TouchableOpacity
                onPress={this._handleOnPress}
                style={styles.buttonStyle}>
                  <Text style={styles.buttonTextStyle}>
                    Show me the magic
                  </Text>
              </TouchableOpacity>
            </View>

            <View style={styles.resultContainer}>
              <TextInput
                style={{textAlign:'center'}}
                multiline={true}
                numberOfLines={7}
                editable={false}
                value={this.state.results}
                underlineColorAndroid="transparent"/>
            </View>
          </Animated.View>
        </View>
    );
  }

  _handleOnPress = () => {
      return fetch('http://10.105.208.209:3000/punny',
        {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            firstParam: this.state.query
          })
        })
        .then((res) => {
          // Log the user's input
          console.log(this.state.query);
          Animated.timing(
            this.state.offsetY,
            { toValue: -100 }
          ).start();

          return res.json()
        })
        .then((resJson) => {
          console.log(resJson);
          this.setState({
            results: resJson['res']['response'][0]['phrase']
          });

          return resJson
        })
        .catch((err) => {
          console.log(err)
          console.log('******')
        })
  };
}

const styles = StyleSheet.create({
  container: {
    flex:1,
    flexDirection:'column',
    justifyContent:'center',
    backgroundColor:'#fff',
  },
  inputContainer: {
    alignItems:'stretch',
  },
  buttonContainer: {
    alignItems:'center',
  },
  resultContainer: {
    paddingTop:100,
    alignItems:'stretch',
  },
  buttonStyle: {
    paddingVertical:15,
  },
  buttonTextStyle: {
    color: "#1E8BC3",
  },
});