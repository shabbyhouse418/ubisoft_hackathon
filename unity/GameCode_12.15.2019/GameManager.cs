using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using LitJson;
using System.IO;
using System.Text;
using System.Data.Common;
//https://github.com/Mervill/UnityLitJson
//https://indienova.com/u/anlideer/blogread/21078

public class Click_dataItem
{
    /// <summary>
    /// 
    /// </summary>
    public string Name { get; set; }
    /// <summary>
    /// 
    /// </summary>
    public int Click_times { get; set; }
    /// <summary>
    /// 
    /// </summary>
    public int Poker_num { get; set; }
}

public class Root
{
    /// <summary>
    /// 
    /// </summary>
    public List<Click_dataItem> Click_data { get; set; }
}

public class GameManager : MonoBehaviour
{
    static int Spade_click_times = 0;
    static int Heart_click_times = 0;
    static int Diamond_click_times = 0;
    static int Club_click_times = 0;
    
    static int Spade_num = 0;
    static int Heart_num = 0;
    static int Diamond_num = 0;
    static int Club_num = 0;

    public int rest_times = 12;
    public Object poker_Spade;
    public Object poker_Heart;
    public Object poker_Diamond;
    public Object poker_Club;

    public Text text_t;

    public SqliteDatabase sqlDB;
    // Start is called before the first frame update
    void Start()
    {
        sqlDB = new SqliteDatabase("data");
        text_t.text = "REST TIMES:"+rest_times;
        readJson();
        initMap();
    }

    public void readSqlite()
    {
        //读取example表中所有数据
        DataTable dt = sqlDB.ExecuteQuery("SELECT * FROM class where id=(select max(id) from class)");
        print(sqlDB.ExecuteQuery("select max(id) from class"));

        foreach (DataRow dr in dt.Rows)
        {
            print((int)dr["CLASS1"]);
            print((int)dr["CLASS2"]);
            print((int)dr["CLASS3"]);
            print((int)dr["CLASS4"]);
            print((int)dr["CLASS5"]);
            print((int)dr["CLASS6"]);
            print((int)dr["CLASS7"]);
            print((int)dr["CLASS8"]);
        }
    }


    // Update is called once per frame
    void Update()
    {

    }
    public void sqlInsert() {
        sqlDB.ExecuteNonQuery("insert into class (CLASS1,CLASS2,CLASS3,CLASS4,CLASS5,CLASS6,CLASS7,CLASS8) values("+ Spade_click_times.ToString() + ","+Heart_click_times.ToString() + "," + Diamond_click_times.ToString() + "," + Club_click_times.ToString() + " ,0,0,0,0)");
    }
    public void setTimes(string name, int times) 
    {
        switch (name)
        {
            case "Spade" : Spade_click_times += times;break;
            case "Heart" : Heart_click_times += times;break;
            case "Diamond" : Diamond_click_times += times;break;
            case "Club" : Club_click_times += times;break;
            default:break;
        }
        
    }

    void readJson()
    {
        string path = Application.dataPath + "/StreamingAssets/click_data.json";
        StreamReader streamreader = new StreamReader(path);//读取数据，转换成数据流
        JsonReader js = new JsonReader(streamreader);//再转换成json数据
        Root r = JsonMapper.ToObject<Root>(js);//读取
        Spade_click_times = r.Click_data[0].Click_times;
        Heart_click_times = r.Click_data[1].Click_times;
        Diamond_click_times = r.Click_data[2].Click_times;
        Club_click_times = r.Click_data[3].Click_times;

        Spade_num = r.Click_data[0].Poker_num;
        Heart_num = r.Click_data[1].Poker_num;
        Diamond_num = r.Click_data[2].Poker_num;
        Club_num = r.Click_data[3].Poker_num;
        
        
    }

    void initMap() 
    {
        Vector3 v2_3 = new Vector3();
        Quaternion q = new Quaternion(0, 0, 0, 0);
        for (int i = 19; i >= 0; i--)
        {
            if (Spade_num > 0)
            {
                Spade_num--;
                v2_3 = pos(i);
                Instantiate(poker_Spade, v2_3, q);
            }
            else if (Heart_num > 0)
            {
                Heart_num--;
                v2_3 = pos(i);
                Instantiate(poker_Heart, v2_3, q);
            }
            else if (Diamond_num > 0)
            {
                Diamond_num--;
                v2_3 = pos(i);
                Instantiate(poker_Diamond, v2_3, q);
            }
            else if (Club_num > 0)
            {
                Club_num--;
                v2_3 = pos(i);
                Instantiate(poker_Club, v2_3, q);
            }
        }
    }

    Vector2 pos(int n) 
    {
        float x = -3.2f + (n % 5) * 1.6f;
        float y = -3.7f + (n / 5) * 2.5f;
        return new Vector2(x, y);
    }


    public void getTimes(string name)
    {
        switch (name)
        {
            case "Spade": Debug.Log("Spade_click_times:"+ Spade_click_times); break;
            case "Heart": Debug.Log("Heart_click_times:" + Heart_click_times); break;
            case "Diamond": Debug.Log("Diamond_click_times:" + Diamond_click_times); break;
            case "Club": Debug.Log("Club_click_times:" + Club_click_times); break;
            default: break;
        }

    }

    public void setText(string s) 
    {
        text_t.text = s;
    }
}
