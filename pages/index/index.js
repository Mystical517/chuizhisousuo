Page(
  {
    data:{
      list_data:[],
      se:'',
      select:[
        {id:1,name:"音乐"},
        {id:2,name:"电影"}
      ],
      position: 'left',
      current: '',


    },
    setse: function (e) {

      this.setData({

        se: e.detail.detail.value

      })

    },
    
    setmusicname:function(e){
      this.setData({
        music_name: e.detail.value
      })
    },

    setmoviename: function (e) {
      this.setData({
        movie_name: e.detail.value
      })
    }
    ,
    /*music_search: function () {
      var str_data=''
      var that = this//不要漏了这句，很重要
      wx.request({
        url: 'http://101.132.132.129:5000/music/'+that.data.music_name,
        headers: {
          'Content-Type': 'application/json'
        },
        success: function (res) {
          var app=getApp()
          app.globalData.music_list_data=res.data
          wx.navigateTo({
            url: '/pages/music/music_search'
          })
        }
      })
    }
    ,
    movie_search: function () {
      var str_data = ''
      var that = this//不要漏了这句，很重要
      wx.request({
        url: 'http://101.132.132.129:5000/movie/' + that.data.movie_name,
        headers: {
          'Content-Type': 'application/json'
        },
        success: function (res) {
          var app = getApp()
          app.globalData.movie_list_data = res.data
          console.log(res.data)
          wx.navigateTo({
            url: '/pages/movie/movie_search'
          })
        }
      })
    }
    ,*/
    selectchange: function ({ detail = {} }){
      this.setData({
        current: detail.value
      });

    }
  ,
    search:function(){
      var str_data = ''
      var that = this
      console.log(that.data.se)
      if (that.data.current === "音乐") {
        wx.request({
          url: 'http://101.132.132.129:5000/music/' + that.data.se,
          headers: {
            'Content-Type': 'application/json'
          },
          success: function (res) {
            var app = getApp()
            app.globalData.music_list_data = res.data
            wx.navigateTo({
              url: '/pages/music/music_search'
            })
          }
        })

      }
      else if (that.data.current === "电影") {
        wx.request({
          url: 'http://101.132.132.129:5000/movie/' + that.data.se,
          headers: {
            'Content-Type': 'application/json'
          },
          success: function (res) {
            var app = getApp()
            app.globalData.music_list_data = res.data
            wx.navigateTo({
              url: '/pages/music/movie_search'
            })
          }
        })

      }
    }
  ,/**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
   
    
  },

   
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    
  }
})