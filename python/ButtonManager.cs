
using UnityEngine;
using UnityEngine.SceneManagement;

public class ButtonManager : MonoBehaviour
{
    // Start is called before the first frame update
    public void goToNextScene()
    {
        SceneManager.LoadScene("Scene2");
    }
}
