import React, { Component, PropTypes } from 'react';
import { AppRegistry, Button, Navigator, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

/**
* :D
* TODO: Add additional screen or visibility/status options, animations
* 
* Parameters that you'll probably care about:
*   query - The string that the user inputs (TODO: client-side validation)
*/

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      text: '',
      query: '',
    };
  }

  render() {
    return (
      <View style={styles.container}>
        <View style={styles.inputContainer}>
          <TextInput
            style={{height:40, textAlign:'center'}}
            placeholder="Type here if you're a cool cat"
            returnKeyLabel={"next"}
            onChangeText={(text) => this.setState({query:text})}
          />
        </View>

        <View style={styles.buttonContainer}>
          <TouchableOpacity
            onPress={this._handleOnPress}
            style={styles.buttonStyle}>
              <Text style={styles.buttonTextStyle}>
                Submit
              </Text>
          </TouchableOpacity>
        </View>
      </View>
    );
  }

  _handleOnPress = () => {
    console.log(this.state.query);
  };
}

const styles = StyleSheet.create({
  container: {
    flex:1,
    flexDirection:'column',
    justifyContent:'center',
    backgroundColor: '#fff',
  },
  inputContainer: {
    alignItems:'stretch',
  },
  buttonContainer: {
    alignItems:'center',
  },
  buttonStyle: {
    paddingVertical:15,
  },
  buttonTextStyle: {
    color: "#1E8BC3",
  },
});
